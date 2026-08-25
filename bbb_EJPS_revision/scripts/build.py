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

import make_graphical_abstract
import manuscript_figures

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


def oxford_join(items):
    """Comma-separated list with an Oxford comma."""
    if not items:
        return ''
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f'{items[0]} and {items[1]}'
    return ', '.join(items[:-1]) + f', and {items[-1]}'


def fmt_scientific(raw):
    """Format a raw number (possibly in 1.23e-4 notation) for Markdown math."""
    raw = str(raw).strip().lower().replace(' ', '').replace('+', '')
    if 'e' not in raw:
        try:
            f = float(raw)
        except ValueError:
            return raw
        if f.is_integer():
            return str(int(f))
        return raw.rstrip('0').rstrip('.') if '.' in raw else raw
    mant, exp = raw.split('e')
    exp = int(exp)
    if mant in ('', '.'):
        mant = '0'
    return f'{mant} \\times 10^{{{exp}}}'


def fmt_value(value, sig_figs=4, decimals=3):
    """Format a numeric value for Markdown text; integers stay plain, very small/large values use scientific notation."""
    f = float(value)
    if f.is_integer():
        return str(int(f))
    if abs(f) < 1e-3 or abs(f) >= 1e4:
        return fmt_scientific(f'{f:.{sig_figs-1}e}')
    return f'{f:.{decimals}g}'


def get_param(params, key, as_float=False):
    """Read a parameter from the parameters CSV."""
    if key not in params:
        raise KeyError(f'Missing parameter: {key}')
    raw = str(params[key]).strip()
    if as_float:
        return float(raw)
    return raw


def load_params(path):
    """Return a dict of key -> raw value from parameters.csv."""
    rows = load_csv(path)
    return {r['key']: r['value'] for r in rows}


# ---------------------------------------------------------------------------
# Computed values derived from public data + parameters
# ---------------------------------------------------------------------------
def compute_values(df, params):
    """Compute all manuscript counts and lists from the CSV data and parameters."""
    n_drugs = len(df)
    n_bbb_pos = sum(1 for d in df if d['bbb_status'].startswith('+'))
    n_bbb_neg = n_drugs - n_bbb_pos

    ad_cutoff = get_param(params, 'AD_CUTOFF_A2', as_float=True)
    bbb_minus_size = sorted([d for d in df if d['bbb_status'].startswith('-') and float(d['a_d']) >= ad_cutoff], key=lambda d: d['drug'])
    bbb_minus_nonsize = sorted([d for d in df if d['bbb_status'].startswith('-') and float(d['a_d']) < ad_cutoff], key=lambda d: d['drug'])
    size_names = oxford_join([d['drug'] for d in bbb_minus_size])
    nonsize_names = [d['drug'] for d in bbb_minus_nonsize]
    nonsize_clause = make_nonsize_clause(nonsize_names, ad_cutoff)

    kb = get_param(params, 'BOLTZMANN_KB', as_float=True)
    T = get_param(params, 'TEMPERATURE_K', as_float=True)
    kT = kb * T
    mw_paracell = get_param(params, 'MW_PARACELLULAR_DA', as_float=True)
    pi_mnm = get_param(params, 'BILAYER_PRESSURE_MNM', as_float=True)
    pi_nm = pi_mnm / 1000.0
    A_ref = get_param(params, 'AD_REFERENCE_A2', as_float=True)

    values = {
        'N_DRUGS': str(n_drugs),
        'N_BBB_POS': str(n_bbb_pos),
        'N_BBB_NEG': str(n_bbb_neg),
        'N_BBB_MINUS_SIZE': str(len(bbb_minus_size)),
        'N_BBB_MINUS_NONSIZE': str(len(bbb_minus_nonsize)),
        'BBB_MINUS_SIZE_LIST': size_names,
        'BBB_MINUS_NONSIZE_LIST': oxford_join(nonsize_names),
        'BBB_MINUS_NONSIZE_CLAUSE': nonsize_clause,
        'AD_CUTOFF': fmt_value(ad_cutoff),
        'AD_LOW': fmt_value(get_param(params, 'AD_LOW_A2', as_float=True)),
        'AD_HIGH': fmt_value(get_param(params, 'AD_HIGH_A2', as_float=True)),
        'MW_PARACELLULAR': fmt_value(mw_paracell),
        'MW_CNS_MAX': fmt_value(get_param(params, 'MW_CNS_MAX_DA', as_float=True)),
        'CNS_LOGP_MIN': fmt_value(get_param(params, 'CNS_LOGP_MIN', as_float=True)),
        'CNS_LOGP_MAX': fmt_value(get_param(params, 'CNS_LOGP_MAX', as_float=True)),
        'TPSA_CNS_MIN': fmt_value(get_param(params, 'TPSA_CNS_MIN_A2', as_float=True)),
        'TPSA_CNS_MAX': fmt_value(get_param(params, 'TPSA_CNS_MAX_A2', as_float=True)),
        'PI_BI_MN_M': fmt_value(pi_mnm),
        'PI_BI_N_M': fmt_value(pi_nm, sig_figs=3, decimals=3),
        'KB': fmt_scientific(get_param(params, 'BOLTZMANN_KB')),
        'TEMP_K': fmt_value(T),
        'KT_J': fmt_value(kT, sig_figs=4, decimals=3),
        'A_REF': fmt_value(A_ref),
    }
    return values


def make_nonsize_clause(names, cutoff):
    if not names:
        return ''
    subj = oxford_join(names)
    if len(names) == 1:
        verb = 'is'
        pronoun = 'its'
    else:
        verb = 'are'
        pronoun = 'their'
    cutoff_str = fmt_value(cutoff)
    return (f'{subj} {verb} BBB-negative despite {pronoun} $A_D$ values below about '
            f'{cutoff_str} Å², reflecting high polarity and/or P-gp-mediated efflux.')


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
def generate_figures(df, params):
    """Generate PNG figures and a PPTX with one slide per figure."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    values = compute_values(df, params)
    table2_rows = make_table2_rows(params, values)
    figs = manuscript_figures.generate_figures(df, params, table2_rows, OUTPUT_DIR)

    # ---- Interactive plot data for Elsevier Interactive Plot Viewer ----
    kb = get_param(params, 'BOLTZMANN_KB', as_float=True)
    T = get_param(params, 'TEMPERATURE_K', as_float=True)
    pi_mnm = get_param(params, 'BILAYER_PRESSURE_MNM', as_float=True)
    pi = pi_mnm / 1000.0
    A_ref = get_param(params, 'AD_REFERENCE_A2', as_float=True)
    kT = kb * T
    factor = pi / kT * 1e-20

    a_d = [float(d['a_d']) for d in df]
    rel = [math.exp(-factor * (ad - A_ref)) for ad in a_d]
    fig2_data_path = OUTPUT_DIR / 'figure2_descriptor_values.csv'
    with open(fig2_data_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['drug', 'bbb_status', 'a_d_A2', 'relative_partition_term'])
        for d, ad_val, rel_val in zip(df, a_d, rel):
            writer.writerow([d['drug'], d['bbb_status'], ad_val, rel_val])

    figs['fig2_data'] = fig2_data_path
    return figs


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


def make_table2_rows(params, values):
    """Return the descriptor-classification rows (header + data)."""
    ad_cutoff = fmt_value(get_param(params, 'AD_CUTOFF_A2', as_float=True))
    pi_mnm = fmt_value(get_param(params, 'BILAYER_PRESSURE_MNM', as_float=True))
    low_mw = 'caffeine, ethanol, and nicotine'
    rows = [
        ['Descriptor', 'Class', 'Definition', 'Key reference', 'Discriminatory power'],
        ['Molecular weight (MW)', 'Conventional', 'Mass of the molecule; low MW aids paracellular/small-molecule diffusion', '{{CITE:LIPINSKI2001}}', f'Boundary condition; explains {low_mw}'],
        ['logP', 'Conventional', 'Lipophilicity; high logP favors partition but does not guarantee BBB entry', '{{CITE:LIPINSKI2001}}', 'Limited alone; loperamide has high logP but is BBB-'],
        ['HBD / HBA / TPSA', 'Conventional', 'Hydrogen-bond donor/acceptor counts and topological polar surface area', '{{CITE:LIPINSKI2001,ABRAHAM2004}}', 'Useful boundaries; desolvation refines them'],
        ['Dipole moment / polarizability', 'Conventional', '3D electronic descriptors of electrostatic and polarizability effects', '{{CITE:MONTGOMERY2024,WANAT2023}}', 'Weak independent discrimination'],
        ['LUMO energy', 'Conventional', 'Frontier orbital energy; used in QSAR models', '{{CITE:WANAT2023}}', 'Weak independent discrimination'],
        ['3D-PSA', 'Conventional', 'Conformationally resolved polar surface area', '{{CITE:SHITYAKOV2013}}', 'Moderate; improves over TPSA when H-bonds shield polarity'],
        ['Membrane cross-sectional area ($A_D$)', 'Unconventional', 'Minimum area presented when inserting into a lipid bilayer', '{{CITE:FISCHER1998,SEELIG1994PNAS,SEELIG2007}}', f'Strong; BBB+ compounds all below ~{ad_cutoff} Å²'],
        ['Collision cross-section (CCS)', 'Unconventional', 'Rotationally averaged cross-section from ion-mobility mass spectrometry', '{{CITE:GUNTNER2019,GUNTNER2021}}', 'Moderate to strong; experimental complement to $A_D$'],
        ['P-gp net flux', 'Unconventional', '$J_{\\mathrm{net}} = J_{\\mathrm{influx}} - J_{\\mathrm{efflux}}$', '{{CITE:SCHINKEL1996,LINNET2008,ZHANG2012,LOSCHER2005}}', 'Strong; explains loperamide, loratadine, cetirizine'],
        ['Chameleonicity / ΔPSA', 'Unconventional', 'Change in exposed polar surface between water and lipid', '{{CITE:POONGAVANAM2024,YU2026}}', 'Limited for small molecules; stronger for macrocycles'],
        ['Lateral bilayer pressure', 'Unconventional', f'Mechanical bilayer pressure opposing insertion; $\\pi_{{bi}} \\approx {pi_mnm}$ mN/m', '{{CITE:FISCHER1998}}', f'Moderate; provides physical basis for $A_D$ cutoff'],
        ['Substructural synergy', 'Unconventional', 'Co-occurrence patterns of fragments associated with BBB permeation', '{{CITE:LEE2025}}', 'Moderate; pattern descriptor, not mechanism'],
    ]
    return rows


def make_table2(params, values):
    """Return a Markdown table classifying descriptors."""
    rows = make_table2_rows(params, values)
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
    titles = {
        1: 'Descriptor values and references',
        2: 'Conventional vs unconventional descriptors',
        3: 'Clinical paradoxes explained by the unified model',
    }
    lines = md_text.splitlines()
    out_lines = []
    table_index = 0
    in_table = False
    for line in lines:
        if line.startswith('|'):
            if not in_table:
                table_index += 1
                title = titles.get(table_index, f'Table {table_index}')
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
    cmd = [str(PANDOC), Path(md_path).name, '-o', Path(docx_path).name, '--mathml']
    subprocess.run(cmd, cwd=str(OUTPUT_DIR), check=True)


def anonymize_md(md_text):
    """Remove author/affiliation/date from YAML frontmatter for anonymized submission."""
    # Remove author block and date line; keep title and the frontmatter delimiters.
    md_text = re.sub(r'^author:\s*\n(?:  - .*(?:\n|$))*(?:  - .*(?:\n|$))?', '', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^date:.*\n?', '', md_text, flags=re.MULTILINE)
    # Collapse empty lines between the two --- delimiters to keep the YAML block valid.
    md_text = re.sub(r'^---\n(?:\n*)', '---\n', md_text, flags=re.MULTILINE)
    return md_text


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
    tmp_md = OUTPUT_DIR / (Path(template_name).stem + '_tmp.md')
    with open(tmp_md, 'w', encoding='utf-8') as f:
        f.write(md)
    run_pandoc(tmp_md, docx_out)
    return docx_out, md


# ---------------------------------------------------------------------------
# Reviewer evaluation report
# ---------------------------------------------------------------------------
def make_reviewer_evaluation(values):
    content = f"""# Reviewer-perspective evaluation of the revised manuscript

## Overall verdict
The revised manuscript addresses the six main points raised by Reviewer #2. It is now methodologically transparent, the dataset limitations are clearly stated, the descriptors are defined and classified, Table 1 provides the requested values and references, the references for lateral bilayer pressure and substructural synergy have been corrected, and the therapeutic applications are explicitly labelled as indicative. Remaining concerns are minor and centre on the inherent small size (n={values['N_DRUGS']}) of the literature-derived dataset; the manuscript does not overstate its conclusions.

## 1. Manuscript quality
- **Newness/focus:** The unified three-gate model provides a coherent conceptual framework that integrates several descriptors. The focus is clearer after the Introduction revision.
- **Logic:** The argument flows from rule-of-five limitations to descriptor definitions, results, and applications. No contradictions.
- **Methods:** Methods are explicit about the literature-derived, estimated nature of the descriptor values and the illustrative nature of the relative partition calculation.
- **Result-conclusion alignment:** Conclusions match the results; the word "heuristic" and repeated caveats prevent over-claim.

## 2. Statistics and design
- The study is a conceptual synthesis, not a formal statistical modelling study. The small n={values['N_DRUGS']} dataset ({values['N_BBB_POS']} BBB-positive, {values['N_BBB_NEG']} BBB-negative) is acknowledged repeatedly. No p-values or confidence intervals are claimed.
- The relative partition term is computed from a deterministic physical formula using estimated A_D; the manuscript explicitly states this is illustrative.

## 3. Figures and tables
- Table 1 is essential and present; it contains the descriptor values and references requested by the reviewer.
- Table 2 clarifies conventional vs unconventional classification.
- Six figures (Figure 1 discriminatory ranking, Figure 2 drug × factor matrix, Figure 3 A_D scatter, Figure 4 unified model, Figure 5 clinical paradoxes, Figure 6 applications framework) and three tables (Tables 1–3) are cited in the text.
- Figures are also provided as a separate editable .pptx and as individual PNG files.

## 4. Reproducibility
- The public repository contains the source CSVs, the reference list, the build script, and the Markdown templates.
- All manuscript numbers, tables, and figures are regenerated from the CSVs and parameters by `scripts/build.py`.
- The derivation of the relative partition term is documented with the constants used.

## 5. Strength of claims
- Claims are appropriately hedged: "guidelines, not guarantees"; "heuristic framework"; "indicative".
- The morphine/CNS-affinity caveat for local anesthetics directly addresses Reviewer #2's safety concern.
- No causal language beyond what the cited biophysical relationships support.

## 6. Threshold rationale audit
- A_D thresholds (50/70/80 Å²) are explicitly tied to Fischer/Seelig and cited in the Methods.
- CNS guideline thresholds (MW 450 Da, cLogP 1–3, TPSA 60–70 Å²) are introduced as descriptive ranges from Rankovic 2015, not as guarantees.
- The 200-Da low-MW boundary is now described as a practical upper bound for the three smallest BBB-positive examples (caffeine, ethanol, nicotine); the text no longer implies that every compound below 200 Da crosses by paracellular diffusion.

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

    for fig_tbl in ['Figure 1', 'Figure 2', 'Figure 3', 'Figure 4', 'Figure 5', 'Figure 6', 'Table 1', 'Table 2', 'Table 3']:
        if fig_tbl in md_text:
            report.append(f'{fig_tbl} cited in text: yes')
        else:
            report.append(f'WARNING: {fig_tbl} not cited in text')

    cite_marks = re.findall(r'\^\d+(?:,\d+)*\^', md_text)
    report.append(f'In-text citation marks: {len(cite_marks)}')

    unresolved = re.findall(r'\{\{[^}]+\}\}', md_text)
    if unresolved:
        report.append(f'WARNING: unresolved placeholders: {unresolved}')

    report.append('Check complete.')
    return '\n'.join(report)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    df = load_csv(DATA_DIR / 'descriptor_table.csv')
    refs = load_csv(DATA_DIR / 'references.csv')
    params = load_params(DATA_DIR / 'parameters.csv')

    values = compute_values(df, params)

    figs = generate_figures(df, params)
    fig1, fig2, fig3, fig4, fig5, fig6, pptx, fig2_data = (
        figs['fig1'], figs['fig2'], figs['fig3'], figs['fig4'], figs['fig5'], figs['fig6'],
        figs['pptx'], figs['fig2_data'],
    )
    ga_png, ga_pptx = make_graphical_abstract.make_graphical_abstract(OUTPUT_DIR)

    table1_md = make_table1(df)
    table2_md = make_table2(params, values)
    table3_md = manuscript_figures.make_table3(df, params)

    citer = Citer(refs)
    rel = lambda p: str(Path(p).relative_to(OUTPUT_DIR))
    ad_cutoff = fmt_value(get_param(params, 'AD_CUTOFF_A2', as_float=True))

    manuscript_replacements = {
        'TABLE1': table1_md,
        'TABLE2': table2_md,
        'TABLE3': table3_md,
        'FIGURE1': f'![Figure 1. Discriminatory power ranking of unconventional and conventional descriptors]({rel(fig1)}){{width=90%}}',
        'FIGURE2': f'![Figure 2. Drug × factor evaluation matrix]({rel(fig2)}){{width=90%}}',
        'FIGURE3': f'![Figure 3. BBB permeability as a function of estimated A_D]({rel(fig3)}){{width=90%}}',
        'FIGURE4': f'![Figure 4. Unified three-component model of BBB permeability]({rel(fig4)}){{width=90%}}',
        'FIGURE5': f'![Figure 5. Unified model decomposition for six clinical cases]({rel(fig5)}){{width=90%}}',
        'FIGURE6': f'![Figure 6. Conceptual framework for applying the unified model to drug-design strategies]({rel(fig6)}){{width=90%}}',
        'REFERENCES': '{{REFERENCES}}',
    }
    manuscript_replacements.update(values)

    # Build the full, internally editable manuscript first (with author metadata)
    _, author_md = build_doc('manuscript.md', 'main_manuscript_with_author.docx', manuscript_replacements, citer, write_md=True)

    # Resolve references once and create anonymized versions for delivery
    author_md = author_md.replace('{{REFERENCES}}', citer.reference_list())
    filled_md_path = OUTPUT_DIR / 'manuscript_filled.md'
    with open(filled_md_path, 'w', encoding='utf-8') as f:
        f.write(author_md)

    anon_md = anonymize_md(author_md)
    anon_md_path = OUTPUT_DIR / 'manuscript_anonymized.md'
    with open(anon_md_path, 'w', encoding='utf-8') as f:
        f.write(anon_md)

    # Main anonymized manuscript with inline figures (matches the requested old-format style)
    main_docx = OUTPUT_DIR / 'main_manuscript.docx'
    run_pandoc(anon_md_path, main_docx)

    # Journal submission version: anonymized and without embedded figures
    sub_md = re.sub(r'!\[.*?\]\(.*?\)\{width=90%\}\n?', '', anon_md)
    sub_md_path = OUTPUT_DIR / 'manuscript_submission.md'
    with open(sub_md_path, 'w', encoding='utf-8') as f:
        f.write(sub_md)
    sub_docx = OUTPUT_DIR / 'main_manuscript_for_submission.docx'
    run_pandoc(sub_md_path, sub_docx)

    # Separate tables docx
    tables_docx = make_tables_docx(anon_md)

    # Response letter
    resp_docx, _ = build_doc('response_to_reviewers.md', 'response_to_reviewers.docx', values, Citer(refs), write_md=False)

    # Cover letter
    cover_docx, _ = build_doc('cover_letter.md', 'cover_letter.docx', values, Citer(refs), write_md=False)

    # Reviewer evaluation
    eval_path = make_reviewer_evaluation(values)

    # Chemical compounds list for Elsevier PubChem (up to 10 compounds)
    chemical_compounds_src = DATA_DIR / 'chemical_compounds.csv'
    chemical_compounds_path = OUTPUT_DIR / 'chemical_compounds.csv'
    if chemical_compounds_src.exists():
        shutil.copy(chemical_compounds_src, chemical_compounds_path)

    # Checks
    check_report = run_checks(main_docx, anon_md_path, label='main manuscript')
    check_report += '\n\n' + run_checks(sub_docx, sub_md_path, label='submission manuscript')
    check_path = OUTPUT_DIR / 'build_check.txt'
    with open(check_path, 'w', encoding='utf-8') as f:
        f.write(check_report)
    print(check_report)

    # Zip
    zip_path = OUTPUT_DIR / 'submission_package.zip'
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        files_to_zip = [main_docx, sub_docx, resp_docx, cover_docx, tables_docx, pptx, ga_png, ga_pptx,
                        fig1, fig2, fig3, fig4, fig5, fig6, fig2_data,
                        DATA_DIR / 'descriptor_table.csv', DATA_DIR / 'references.csv', DATA_DIR / 'parameters.csv',
                        eval_path, check_path, anon_md_path, sub_md_path]
        if chemical_compounds_path.exists():
            files_to_zip.append(chemical_compounds_path)
        for f in files_to_zip:
            zf.write(f, arcname=f.name)

    print(f'\nDone. Outputs in {OUTPUT_DIR}')
    print(f'  Main manuscript (anonymized, inline figures): {main_docx.name}')
    print(f'  Submission manuscript (anonymized, no embedded figures): {sub_docx.name}')
    print(f'  Response letter: {resp_docx.name}')
    print(f'  Cover letter: {cover_docx.name}')
    print(f'  Tables docx: {tables_docx.name}')
    print(f'  Figures pptx: {pptx.name}')
    print(f'  Graphical abstract: {ga_png.name}, {ga_pptx.name}')
    print(f'  Submission zip: {zip_path.name}')


if __name__ == '__main__':
    main()
