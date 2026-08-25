# EJPS BBB-permeability manuscript revision

Source files for the revised manuscript *Unconventional Molecular Descriptors for Blood–Brain Barrier Permeability Prediction: A Unified Model and Its Implications for Local Anesthetic Design, Micellar Formulation, and Chelation-Based Effect Modification* (Ms. No. PHASCI-D-26-00475, *European Journal of Pharmaceutical Sciences*).

## Source files

- `manuscript.md` – main text in Pandoc-flavored Markdown with `{{CITE:KEY}}` placeholders
- `cover_letter.md` – cover letter to the Section Editor
- `response_to_reviewers.md` – point-by-point response to Reviewer #2
- `data/descriptor_table.csv` – 24-drug descriptor matrix used for Table 1
- `data/parameters.csv` – physical constants and thresholds used for calculations
- `data/references.csv` – 28-entry reference database used to resolve citations
- `scripts/build.py` – reproducible build pipeline
- `scripts/manuscript_figures.py` – generator for the 6 figures and editable `figures.pptx`

## Build outputs

All generated files are written to `output/`:

- `main_manuscript.docx` – inline figures and tables with Word OMML equations
- `main_manuscript_for_submission.docx` – same text/tables, figures removed for separate upload
- `response_to_reviewers.docx`
- `cover_letter.docx`
- `tables.docx` – editable tables on their own
- `figures.pptx` – editable PowerPoint, one figure per slide
- `figure1_discriminatory_power.png`, `figure2_drug_factor_matrix.png`, `figure3_ad_scatter.png`, `figure4_unified_model.png`, `figure5_clinical_paradoxes.png`, `figure6_applications.png`
- `graphical_abstract.png`, `graphical_abstract.pptx`
- `figure2_descriptor_values.csv` – source data for interactive plot submission
- `submission_package.zip` – complete submission file set
- `reviewer_evaluation.md` – reviewer-perspective critical review
- `build_check.txt` – automated checks report

## Dependencies

- Python 3.10+
- `pandoc` 3.1+ with `--mathml` support
- Python packages listed in `requirements.txt`

## Rebuild everything

```bash
cd bbb_EJPS_revision
pip install -r requirements.txt
python3 scripts/build.py
```

The pipeline reads the CSVs and Markdown templates, computes the relative partition term from the lateral bilayer pressure model, resolves citations in Vancouver order, generates figures and tables, and writes the Word files and submission package. No numbers are hard-coded in the manuscript.

## Data provenance

Descriptor values and BBB classifications were estimated from published structural data, binding/efflux reports, and validated biophysical relationships. The exact sources are given in `data/descriptor_table.csv` and the references in `data/references.csv`.
