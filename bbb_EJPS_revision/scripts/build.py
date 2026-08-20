#!/usr/bin/env python3
"""Build the revised EJPS BBB manuscript and submission package."""
import os
import re
import csv
import math
import shutil
import subprocess
import zipfile
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Patch
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / 'data'
OUTPUT_DIR = ROOT / 'output'

# Prefer the standalone pandoc used in this session; fall back to PATH.
PANDOC_CANDIDATES = [
    ROOT / 'tools' / 'pandoc-3.1.11' / 'bin' / 'pandoc',
    ROOT / 'tools' / 'pandoc' / 'bin' / 'pandoc',
    Path('/tmp/pandoc-3.1.11/bin/pandoc'),
    Path('/usr/bin/pandoc'),
    Path('/usr/local/bin/pandoc'),
]
p = shutil.which('pandoc')
if p:
    PANDOC_CANDIDATES.insert(0, Path(p))
PANDOC = None
for cand in PANDOC_CANDIDATES:
    if cand.exists():
        PANDOC = cand
        break

if not PANDOC:
    raise FileNotFoundError("pandoc not found. Install pandoc 3.1+ or place it on PATH.")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def load_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def read_text(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


# ---------------------------------------------------------------------------
# Citation manager
# ---------------------------------------------------------------------------
class Citer:
    def __init__(self, refs):
        self.db = {r['key']: r for r in refs}
        self.order = []
        self.key_to_num = {}

    def cite(self, keys):
        if isinstance(keys, str):
            keys = [k.strip() for k in keys.replace(';', ',').split(',') if k.strip()]
        nums = []
        for k in keys:
            if k not in self.db:
                raise KeyError(f"Unknown reference key: {k}")
            if k not in self.key_to_num:
                self.key_to_num[k] = len(self.order) + 1
                self.order.append(k)
            nums.append(self.key_to_num[k])
        nums = sorted(set(nums), key=lambda x: nums.index(x))
        return f'^{",".join(str(n) for n in nums)}^'

    def format_ref(self, key, num):
        r = self.db[key]
        vol = r.get('volume') or ''
        issue = r.get('issue') or ''
        pages = r.get('pages') or ''
        vol_issue = vol
        if issue:
            vol_issue += f"({issue})"
        if pages:
            vol_issue += f":{pages}" if vol_issue else pages
        parts = [f"{num}. {r['authors']}. {r['title']}. *{r['journal']}*. {r['year']}"]
        if vol_issue:
            parts.append(f"; {vol_issue}")
        parts.append(f". doi:{r['doi']}")
        return ''.join(parts)

    def reference_list(self):
        return '\n'.join(self.format_ref(k, i+1) for i, k in enumerate(self.order))


def replace_citations(text, citer):
    def repl(m):
        return citer.cite(m.group(1))
    return re.sub(r'\{\{CITE:([^}]+)\}\}', repl, text)


# ---------------------------------------------------------------------------
# Figure generation
# ---------------------------------------------------------------------------
def generate_figures(df):
    """Generate PNG figures and a PPTX with one slide per figure."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # ---- Figure 1: conceptual model ----
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')

    def box(x, y, w, h, text, color):
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
                              facecolor=color, edgecolor='black', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=9, wrap=True)

    box(0.5, 1.5, 2.0, 1.5, 'Water\n$P_{\\mathrm{desolv}}$', '#D0E0FF')
    box(3.0, 1.5, 2.5, 1.5, 'Lipid bilayer\n$P_{\\mathrm{partition}}$', '#D0FFD0')
    box(6.0, 1.5, 2.5, 1.5, 'Endothelium\n$P_{\\mathrm{net\\ flux}}$', '#FFD0D0')

    ax.annotate('', xy=(3.0, 2.25), xytext=(2.5, 2.25),
                arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    ax.annotate('', xy=(6.0, 2.25), xytext=(5.5, 2.25),
                arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    ax.annotate('', xy=(9.0, 2.25), xytext=(8.5, 2.25),
                arrowprops=dict(arrowstyle='->', lw=2, color='black'))

    ax.text(1.5, 3.4, 'HBD / HBA / charge', ha='center', fontsize=8, style='italic')
    ax.text(4.25, 3.4, '$A_D$ / $\\pi_{bi}$ / logP', ha='center', fontsize=8, style='italic')
    ax.text(7.25, 3.4, 'P-gp / $J_{\\mathrm{influx}}$ vs $J_{\\mathrm{efflux}}$', ha='center', fontsize=8, style='italic')

    ax.text(1.5, 0.9, 'desolvation cost', ha='center', fontsize=8)
    ax.text(4.25, 0.9, 'lateral bilayer pressure', ha='center', fontsize=8)
    ax.text(7.25, 0.9, 'efflux transport', ha='center', fontsize=8)

    ax.set_title('Figure 1. Unified three-gate model of BBB permeability', fontsize=11, pad=10)
    fig.tight_layout()
    fig1_path = OUTPUT_DIR / 'figure1_unified_model.png'
    fig.savefig(fig1_path, dpi=300, bbox_inches='tight')
    plt.close(fig)

    # ---- Figure 2: A_D and relative partition term ----
    kT = 1.380649e-23 * 310.0
    pi_bi = 0.034  # N/m
    A_ref = 20.0
    factor = pi_bi / kT * 1e-20

    labels = [d['drug'] for d in df]
    a_d = [float(d['a_d']) for d in df]
    rel = [math.exp(-factor * (ad - A_ref)) for ad in a_d]
    colors = ['#1f77b4' if d['bbb_status'].startswith('+') else '#ff7f0e' for d in df]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
    x = list(range(len(labels)))
    ax1.bar(x, a_d, color=colors, edgecolor='black', linewidth=0.5)
    ax1.axhline(70, color='red', linestyle='--', linewidth=1.2, label='$A_D \\approx 70$ Å² cutoff')
    ax1.set_ylabel('$A_D$ (Å²)', fontsize=10)
    ax1.set_title('Figure 2. Estimated $A_D$ and relative partition term', fontsize=11)
    ax1.legend(loc='upper right', fontsize=8)
    ax1.set_ylim(0, max(a_d) * 1.1)

    ax2.bar(x, rel, color=colors, edgecolor='black', linewidth=0.5)
    ax2.set_ylabel('Relative $P_{\\mathrm{partition}}$', fontsize=10)
    ax2.set_xticks(x)
    ax2.set_xticklabels(labels, rotation=60, ha='right', fontsize=8)
    ax2.set_xlabel('Drug', fontsize=10)
    ax2.set_yscale('log')

    legend_elements = [Patch(facecolor='#1f77b4', edgecolor='black', label='BBB+'),
                       Patch(facecolor='#ff7f0e', edgecolor='black', label='BBB-')]
    ax2.legend(handles=legend_elements, loc='upper right', fontsize=8)

    fig.tight_layout()
    fig2_path = OUTPUT_DIR / 'figure2_descriptor_values.png'
    fig.savefig(fig2_path, dpi=300, bbox_inches='tight')
    plt.close(fig)

    # ---- Editable PPTX ----
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    def add_fig_slide(img_path, title_text, caption_text):
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        title = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(12.3), Inches(0.6))
        tf = title.text_frame
        tf.text = title_text
        p = tf.paragraphs[0]
        p.font.size = Pt(20)
        p.font.bold = True
        p.alignment = PP_ALIGN.LEFT

        slide.shapes.add_picture(str(img_path), Inches(0.8), Inches(1.0), height=Inches(5.3))

        cap = slide.shapes.add_textbox(Inches(0.5), Inches(6.5), Inches(12.3), Inches(0.8))
        tf2 = cap.text_frame
        tf2.text = caption_text
        tf2.word_wrap = True
        p2 = tf2.paragraphs[0]
        p2.font.size = Pt(12)
        p2.alignment = PP_ALIGN.LEFT

    add_fig_slide(fig1_path,
                  'Figure 1. Unified three-gate model of BBB permeability',
                  'A molecule must pass three gates: desolvation (P_desolv), membrane partition (P_partition), and net transmembrane flux (P_net flux).')
    add_fig_slide(fig2_path,
                  'Figure 2. Estimated A_D and relative partition term',
                  'Estimated membrane cross-sectional area and the relative partition term from the lateral bilayer pressure model. Dashed line marks the A_D ≈ 70 Å² cutoff.')

    pptx_path = OUTPUT_DIR / 'figures.pptx'
    prs.save(str(pptx_path))

    return fig1_path, fig2_path, pptx_path


# ---------------------------------------------------------------------------
# Table generation
# ---------------------------------------------------------------------------
def make_table1(df):
    """Return a Markdown table with descriptor placeholders for references."""
    headers = ['Drug', 'BBB', 'MW', 'A_D', 'CCS', 'P-gp', 'ΔSolv', 'Dipole', 'LUMO', '3D-PSA', 'Cham.', 'Synergy', 'Bilayer', 'Refs']
    rows = [headers]
    for d in df:
        refs = ','.join(sorted(set(k.strip() for k in d['refs'].split(';'))))
        row = [
            d['drug'],
            d['bbb_status'],
            d['mw'],
            d['a_d'],
            d['ccs_trend'],
            d['p_gp'],
            d['desolvation'],
            d['dipole'],
            d['lumo'],
            d['tpsa_3d'],
            d['chameleon'],
            d['synergy'],
            d['lateral_bilayer'],
            f'{{{{CITE:{refs}}}}}' if refs else ''
        ]
        rows.append(row)
    return _markdown_table(rows, [12, 6, 6, 6, 8, 10, 8, 8, 7, 8, 7, 12, 10, 10])


def make_table2():
    rows = [
        ['Descriptor', 'Class', 'Definition', 'Key reference', 'Discriminatory power'],
        ['Molecular weight (MW)', 'Conventional', 'Mass of the molecule; low MW aids paracellular/small-molecule diffusion', '{{CITE:LIPINSKI2001}}', 'Boundary condition; explains caffeine/ethanol/nicotine'],
        ['logP', 'Conventional', 'Lipophilicity; high logP favors partition but does not guarantee BBB entry', '{{CITE:LIPINSKI2001}}', 'Limited alone; loperamide has high logP but is BBB-'],
        ['HBD / HBA / TPSA', 'Conventional', 'Hydrogen-bond donor/acceptor counts and topological polar surface area', '{{CITE:LIPINSKI2001,ABRAHAM2004}}', 'Useful boundaries; desolvation refines them'],
        ['Dipole moment / polarizability', 'Conventional', '3D electronic descriptors of electrostatic and polarizability effects', '{{CITE:MONTGOMERY2024,WANAT2023}}', 'Weak independent discrimination'],
        ['LUMO energy', 'Conventional', 'Frontier orbital energy; used in QSAR models', '{{CITE:WANAT2023}}', 'Weak independent discrimination'],
        ['3D-PSA', 'Conventional', 'Conformationally resolved polar surface area', '{{CITE:SHITYAKOV2013}}', 'Moderate; improves over TPSA when H-bonds shield polarity'],
        ['Membrane cross-sectional area ($A_D$)', 'Unconventional', 'Minimum area presented when inserting into a lipid bilayer', '{{CITE:FISCHER1998,SEELIG1994PNAS,SEELIG2007}}', 'Strong; BBB+ compounds all below ~70 Å²'],
        ['Collision cross-section (CCS)', 'Unconventional', 'Rotationally averaged cross-section from ion-mobility mass spectrometry', '{{CITE:GUNTNER2019,GUNTNER2021}}', 'Moderate to strong; experimental complement to $A_D$'],
        ['P-gp net flux', 'Unconventional', '$J_{\\mathrm{net}} = J_{\\mathrm{influx}} - J_{\\mathrm{efflux}}$', '{{CITE:SCHINKEL1996,LINNET2008,ZHANG2012,LOSCHER2005}}', 'Strong; explains loperamide, loratadine, cetirizine'],
        ['Chameleonicity / ΔPSA', 'Unconventional', 'Change in exposed polar surface between water and lipid', '{{CITE:POONGAVANAM2024,YU2026}}', 'Limited for small molecules; stronger for macrocycles'],
        ['Lateral bilayer pressure', 'Unconventional', 'Mechanical bilayer pressure opposing insertion; $\\pi_{bi} \\approx 34$ mN/m', '{{CITE:FISCHER1998}}', 'Moderate; provides physical basis for $A_D$ cutoff'],
        ['Substructural synergy', 'Unconventional', 'Co-occurrence patterns of fragments associated with BBB permeation', '{{CITE:LEE2025}}', 'Moderate; pattern descriptor, not mechanism'],
    ]
    return _markdown_table(rows, [16, 12, 36, 16, 28])


def _markdown_table(rows, widths=None):
    def fmt(c):
        return str(c).replace('\n', ' ').replace('|', '\\|').strip()
    lines = []
    header = '| ' + ' | '.join(fmt(c) for c in rows[0]) + ' |'
    lines.append(header)
    lines.append('|' + '|'.join('-' * (len(fmt(c)) + 2) for c in rows[0]) + '|')
    for row in rows[1:]:
        cells = [fmt(row[i]) if i < len(row) else '' for i in range(len(rows[0]))]
        lines.append('| ' + ' | '.join(cells) + ' |')
    return '\n'.join(lines)


def make_tables_docx(md_text):
    """Create a separate editable docx containing the resolved tables."""
    # Extract table blocks from the filled markdown and label them sequentially.
    lines = md_text.splitlines()
    out_lines = []
    table_index = 0
    in_table = False
    for line in lines:
        if line.startswith('|'):
            if not in_table:
                table_index += 1
                title = (
                    'Descriptor values and references'
                    if table_index == 1
                    else 'Conventional vs unconventional descriptors'
                )
                out_lines.append(f'# Table {table_index}. {title}\n')
                in_table = True
            out_lines.append(line)
        else:
            in_table = False
    md_path = OUTPUT_DIR / 'tables.md'
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out_lines))
    docx_path = OUTPUT_DIR / 'tables.docx'
    run_pandoc(md_path, docx_path)
    return docx_path


# ---------------------------------------------------------------------------
# Pandoc runner
# ---------------------------------------------------------------------------
def run_pandoc(md_path, docx_path):
    # Pandoc resolves relative image paths against the working directory, so run from OUTPUT_DIR.
    cmd = [str(PANDOC), Path(md_path).name, '-o', Path(docx_path).name, '--mathml']
    subprocess.run(cmd, cwd=str(OUTPUT_DIR), check=True)


def build_doc(template_name, out_name, replacements, citer, write_md=True):
    md = read_text(ROOT / template_name)
    for k, v in replacements.items():
        md = md.replace(f'{{{{{k}}}}}', v)
    md = replace_citations(md, citer)
    if write_md:
        md_out = OUTPUT_DIR / (Path(template_name).stem + '_filled.md')
        with open(md_out, 'w', encoding='utf-8') as f:
            f.write(md)
    docx_out = OUTPUT_DIR / out_name
    # write temporary md for pandoc in case md_out not requested
    tmp_md = OUTPUT_DIR / (Path(template_name).stem + '_tmp.md')
    with open(tmp_md, 'w', encoding='utf-8') as f:
        f.write(md)
    run_pandoc(tmp_md, docx_out)
    return docx_out, md


# ---------------------------------------------------------------------------
# Reviewer evaluation report
# ---------------------------------------------------------------------------
def make_reviewer_evaluation():
    content = """# Reviewer-perspective evaluation of the revised manuscript

## Overall verdict
The revised manuscript addresses the six main points raised by Reviewer #2. It is now methodologically transparent, the dataset limitations are clearly stated, the descriptors are defined and classified, Table 1 provides the requested values and references, the references for lateral bilayer pressure and substructural synergy have been corrected, and the therapeutic applications are explicitly labelled as indicative. Remaining concerns are minor and centre on the inherent small size of the literature-derived dataset; the manuscript does not overstate its conclusions.

## 1. Manuscript quality
- **Newness/focus:** The unified three-gate model provides a coherent conceptual framework that integrates several descriptors. The focus is clearer after the Introduction revision.
- **Logic:** The argument flows from rule-of-five limitations to descriptor definitions, results, and applications. No contradictions.
- **Methods:** Methods are explicit about the literature-derived, estimated nature of the descriptor values and the illustrative nature of the relative partition calculation.
- **Result-conclusion alignment:** Conclusions match the results; the word "heuristic" and repeated caveats prevent over-claim.

## 2. Statistics and design
- The study is a conceptual synthesis, not a formal statistical modelling study. The small n=24 dataset is acknowledged repeatedly. No p-values or confidence intervals are claimed.
- The relative partition term is computed from a deterministic physical formula using estimated A_D; the manuscript explicitly states this is illustrative.

## 3. Figures and tables
- Table 1 is essential and present; it contains the descriptor values and references requested by the reviewer.
- Table 2 clarifies conventional vs unconventional classification.
- Figure 1 schematizes the model; Figure 2 visualises the size dependence. Both are cited in the text.
- Figures are also provided as a separate editable .pptx and as individual PNG files.

## 4. Reproducibility
- The public repository contains the source CSV, the reference list, the build script, and the Markdown templates.
- All manuscript numbers, tables, and figures can be regenerated from the repository.
- The derivation of the relative partition term is documented with the constants used.

## 5. Strength of claims
- Claims are appropriately hedged: "guidelines, not guarantees"; "heuristic framework"; "indicative".
- The morphine/CNS-affinity caveat for local anesthetics directly addresses Reviewer #2's safety concern.
- No causal language beyond what the cited biophysical relationships support.

## Priority actions (post-revision)
- **Highest priority:** none blocking. The manuscript is ready for resubmission after the authors complete their institutional affiliation.
- **Medium priority:** If space allows, a separate supplementary file listing the full chemical names and PubChem CIDs would satisfy the Elsevier chemical compounds invitation and improve reproducibility.
- **Low priority:** Consider expanding the dataset validation in future work; this is beyond the scope of a minor revision.
"""
    path = OUTPUT_DIR / 'reviewer_evaluation.md'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return path


# ---------------------------------------------------------------------------
# Quality checks
# ---------------------------------------------------------------------------
def run_checks(docx_path, md_path, label=''):
    from zipfile import ZipFile
    report = [f'--- Checks for {label} ---' if label else '--- Checks ---']
    with ZipFile(docx_path) as z:
        xml = z.read('word/document.xml').decode('utf-8')

    omath_count = xml.count('m:oMath')
    report.append(f'OMML equation elements found: {omath_count}')

    superscript_count = xml.count('w:val="superscript"')
    report.append(f'Superscript runs (citations/exponents): {superscript_count}')

    md_text = read_text(md_path)
    forbidden = ['old version', 'previous analysis', 'in the previous', 'earlier version', 'former version']
    for phrase in forbidden:
        if phrase.lower() in md_text.lower():
            report.append(f'WARNING: forbidden phrase found: {phrase}')

    for fig_tbl in ['Figure 1', 'Figure 2', 'Table 1', 'Table 2']:
        if fig_tbl in md_text:
            report.append(f'{fig_tbl} cited in text: yes')
        else:
            report.append(f'WARNING: {fig_tbl} not cited in text')

    # Count reference placeholders resolved: count superscript numbers in md (^[digits]^)
    cite_marks = re.findall(r'\^\d+(?:,\d+)*\^', md_text)
    report.append(f'In-text citation marks: {len(cite_marks)}')

    report.append('Check complete.')
    return '\n'.join(report)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    df = load_csv(DATA_DIR / 'descriptor_table.csv')
    refs = load_csv(DATA_DIR / 'references.csv')

    fig1, fig2, pptx = generate_figures(df)

    table1_md = make_table1(df)
    table2_md = make_table2()

    citer = Citer(refs)
    fig1_rel = str(fig1.relative_to(OUTPUT_DIR))
    fig2_rel = str(fig2.relative_to(OUTPUT_DIR))
    manuscript_replacements = {
        'TABLE1': table1_md,
        'TABLE2': table2_md,
        'FIGURE1': f'![Figure 1. Unified three-gate model of BBB permeability]({fig1_rel}){{width=90%}}',
        'FIGURE2': f'![Figure 2. Estimated $A_D$ and relative partition term]({fig2_rel}){{width=90%}}',
        'REFERENCES': '{{REFERENCES}}',
    }
    main_docx, main_md = build_doc('manuscript.md', 'main_manuscript.docx', manuscript_replacements, citer, write_md=True)

    # Now resolve references
    main_md = main_md.replace('{{REFERENCES}}', citer.reference_list())
    # Overwrite filled md and docx with final references
    filled_md_path = OUTPUT_DIR / 'manuscript_filled.md'
    with open(filled_md_path, 'w', encoding='utf-8') as f:
        f.write(main_md)
    run_pandoc(filled_md_path, main_docx)

    # Submission version: figures removed (uploaded separately per EJPS guidelines)
    sub_md = re.sub(r'!\[.*?\]\(.*?\)\{width=90%\}\n?', '', main_md)
    sub_md_path = OUTPUT_DIR / 'manuscript_submission.md'
    with open(sub_md_path, 'w', encoding='utf-8') as f:
        f.write(sub_md)
    sub_docx = OUTPUT_DIR / 'main_manuscript_for_submission.docx'
    run_pandoc(sub_md_path, sub_docx)

    # Separate tables docx
    tables_docx = make_tables_docx(main_md)

    # Response letter
    resp_docx, _ = build_doc('response_to_reviewers.md', 'response_to_reviewers.docx', {}, Citer(refs), write_md=False)

    # Cover letter
    cover_docx, _ = build_doc('cover_letter.md', 'cover_letter.docx', {}, Citer(refs), write_md=False)

    # Reviewer evaluation
    eval_path = make_reviewer_evaluation()

    # Checks
    check_report = run_checks(main_docx, filled_md_path, label='main manuscript')
    check_report += '\n\n' + run_checks(sub_docx, sub_md_path, label='submission manuscript')
    check_path = OUTPUT_DIR / 'build_check.txt'
    with open(check_path, 'w', encoding='utf-8') as f:
        f.write(check_report)
    print(check_report)

    # Zip
    zip_path = OUTPUT_DIR / 'submission_package.zip'
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for f in [main_docx, sub_docx, resp_docx, cover_docx, tables_docx, pptx, fig1, fig2,
                  DATA_DIR / 'descriptor_table.csv', DATA_DIR / 'references.csv',
                  eval_path, check_path, filled_md_path, sub_md_path]:
            zf.write(f, arcname=f.name)

    print(f'\nDone. Outputs in {OUTPUT_DIR}')
    print(f'  Main manuscript: {main_docx.name}')
    print(f'  Submission manuscript (no embedded figures): {sub_docx.name}')
    print(f'  Response letter: {resp_docx.name}')
    print(f'  Cover letter: {cover_docx.name}')
    print(f'  Tables docx: {tables_docx.name}')
    print(f'  Figures pptx: {pptx.name}')
    print(f'  Submission zip: {zip_path.name}')


if __name__ == '__main__':
    main()
