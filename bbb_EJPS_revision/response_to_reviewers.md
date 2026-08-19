---
title: "Response to Reviewer Comments"
author: "Tatsuki Onishi"
date: "19 August 2026"
---

**Manuscript:** Unconventional Molecular Descriptors for Blood–Brain Barrier Permeability Prediction: A Unified Model and Its Implications for Local Anesthetic Design, Micellar Formulation, and Chelation-Based Effect Modification  
**Journal:** European Journal of Pharmaceutical Sciences  
**Manuscript number:** PHASCI-D-26-00475

We thank Reviewer #2 for the constructive comments. Below we address each point and indicate where changes have been made in the revised manuscript.

---

## Reviewer #2, Comment 1

> "In the Introduction the rule of 5 is stated as a prerequisite for BBB permeability and the paradoxes discussed later (caffeine, loperamide) are based on this... Rule of 5 and any other rule of thumb does not guarantee permeability. Lipinski's rule of 5 is proposed for orally administered drugs... this paragraph in the Introduction should be revised."

**Response.** We have revised the Introduction to state explicitly that Lipinski's rule of five and the related CNS guidelines are guidelines, not guarantees, and that Lipinski's rule was originally developed for oral drug absorption (page 1, Introduction). The text now emphasizes that adherence to these rules predicts a lower risk of absorption/permeability problems but does not ensure BBB permeation. The paradoxes (caffeine, loperamide, morphine/heroin) are framed as illustrations of why additional descriptors are needed, not as violations of a prerequisite.

---

## Reviewer #2, Comment 2

> "17 BBB+ and 7 BBB- drugs are rather limited number to draw sound conclusions. Among them three drugs, caffeine, ethanol and nicotine have molecular weight below 200, so their BBB penetration can simply justified by paracellular diffusion."

**Response.** We agree. We added a clear limitation statement in the Abstract, Methods, Results, and Discussion noting that the dataset is small and that conclusions are therefore tentative (pages 1–5). We also added explicit text stating that caffeine, ethanol, and nicotine are small enough to cross by paracellular or small-molecule diffusion, so their permeability does not depend solely on lipid-membrane partitioning (Results, page 4; Discussion, page 5).

---

## Reviewer #2, Comment 3

> "The authors should describe with a few words the descriptors which could be considered as unconventional... The role of molecular weight should also be considered."

**Response.** We added a dedicated Methods subsection that defines each descriptor and classifies it as conventional or unconventional (page 2–3). Unconventional descriptors are membrane cross-sectional area ($A_D$), collision cross-section (CCS), P-gp net flux, chameleonicity/ΔPSA, lateral bilayer pressure, and substructural synergy. Conventional descriptors are molecular weight, logP, TPSA, HBD, HBA, dipole moment/polarizability, LUMO energy, and 3D-PSA. Table 2 summarizes the classification and the rationale. We also discuss molecular weight explicitly as a conventional boundary condition rather than as a mechanistic descriptor.

---

## Reviewer #2, Comment 4

> "The authors should present in a table the values of the descriptors used for each drug and the relevant reference."

**Response.** Table 1 now reports, for each of the 24 drugs, the BBB status, molecular weight, $A_D$, CCS trend, desolvation cost, P-gp substrate status, dipole, LUMO, 3D-PSA, chameleonicity, substructural synergy, lateral bilayer pressure effect, net-flux scenario, and the relevant literature references (page 3). The complete numerical matrix is also provided as a supplementary CSV file.

---

## Reviewer #2, Comment 5

> "The reference for Lateral bilayer pressure is not relevant. The reference for Substructural synergy is wrong."

**Response.** We corrected both references. The lateral bilayer pressure model is now cited to Fischer, Gottschlich and Seelig, *J Membr Biol* 1998, 165:201–211, which reports the BBB-mimicking bilayer pressure $\pi_{bi} \approx 34\ \mathrm{mN/m}$ and the exponential relationship between $A_D$ and partitioning (Methods and Table 1). The substructural synergy descriptor is now cited to Lee, Jun, Kim et al., *Comput Biol Med* 2025, DOI 10.1016/j.compbiomed.2025.111183 (Methods and Table 1).

---

## Reviewer #2, Comment 6

> "In regard to the applications the suggestions of the authors should be only indicative due to the limited drugs study. More to the point as far as local anesthetics are concerned... their affinity to receptors within CNS is always an issue, since with very high affinity even low penetration is capable to produce undesired effects (the example of morphine)."

**Response.** We have re-written the Applications and Discussion sections to state explicitly that all therapeutic suggestions are indicative and require experimental validation (Abstract, Methods, Discussion, page 5). For local anesthetics, we now emphasize that minimizing BBB passive permeability is not sufficient to avoid CNS side effects: high CNS receptor affinity can produce central effects at low brain concentrations, as illustrated by morphine (Discussion, page 5). We added the same caveats to the micellar formulation and chelation sections.

---

## Additional changes

- We clarified the distinction between guidelines and guarantees for Lipinski's and CNS rules throughout the Introduction.
- We added a limitation paragraph on the small dataset and paracellular diffusion for low-MW compounds.
- We added explicit definitions and conventional/unconventional classifications for all descriptors.
- We added Table 1 and Table 2 and cited them in the text.
- We corrected the references for lateral bilayer pressure and substructural synergy.
- We toned down all therapeutic applications and added the morphine/CNS-affinity caveat for local anesthetics.
- We removed any language that could be read as referring to an earlier version of the analysis.
