---
title: "Unconventional Molecular Descriptors for Blood–Brain Barrier Permeability Prediction: A Unified Model and Its Implications for Local Anesthetic Design, Micellar Formulation, and Chelation-Based Effect Modification"
author:
  - "Tatsuki Onishi"
  - "[Affiliation to be inserted]"
date: "19 August 2026"
---

# Highlights

- A unified three-gate probabilistic framework treats BBB permeability as the product of desolvation, membrane partition, and net transmembrane flux, integrating both conventional and unconventional molecular descriptors.
- Membrane cross-sectional area ($A_D$) and P-glycoprotein net flux are the most discriminatory unconventional factors in the curated {{N_DRUGS}}-drug dataset, clearly separating BBB-permeable from most BBB-poor compounds.
- The model explains classic BBB paradoxes within a single picture: caffeine, ethanol, and nicotine can cross partly by paracellular or small-molecule diffusion at very low molecular weight; loperamide is excluded by strong P-gp efflux despite high lipophilicity; and heroin, codeine, and morphine differ mainly by desolvation cost.
- Conventional descriptors (MW, logP, TPSA, HBD/HBA, dipole moment/polarizability, LUMO, 3D-PSA) are distinguished from unconventional membrane- and transport-specific descriptors, with explicit definitions and supporting references provided in a dedicated table.
- Therapeutic directions for reduced-CNS-toxicity local anesthetics, micellar formulations, and chelation-based effect modification are presented as hypothesis-generating, indicative ideas that require experimental validation in larger datasets.

# Abstract

**Background.** Predicting blood–brain barrier (BBB) permeability remains a central problem in central nervous system (CNS) drug design. Conventional rules such as Lipinski's rule of five and related CNS guidelines describe physicochemical boundaries but do not guarantee permeability.
**Objective.** We examined how a set of molecular descriptors—including membrane cross-sectional area, collision cross-section, P-glycoprotein (P-gp) net flux, desolvation cost, chameleonicity, 3D polar surface area, dipole moment/polarizability, LUMO energy, substructural synergy, and lateral bilayer pressure—can be integrated into a single probabilistic framework.
**Methods.** A curated set of {{N_DRUGS}} drugs ({{N_BBB_POS}} BBB-permeable, {{N_BBB_NEG}} BBB-poor) was compiled from the published literature. Descriptor values were estimated from public structural data, published binding/efflux data, and validated biophysical relationships; the relative membrane-partition term was calculated from the lateral bilayer pressure model.
**Results.** Membrane cross-sectional area ($A_D$) and P-gp net flux discriminated BBB-positive from BBB-negative compounds most clearly. Desolvation cost distinguished morphine from heroin and codeine, and lateral bilayer pressure provided a physical rationale for the exponential size dependence of membrane partitioning. Caffeine, ethanol, and nicotine, all with molecular weight below {{MW_PARACELLULAR}} Da, are examples of small molecules that can cross by paracellular or small-molecule diffusion, so their permeability does not rely solely on lipid-membrane partitioning.
**Conclusions.** BBB permeability can be framed as the product of three gated probabilities: desolvation, membrane partition, and net transmembrane flux. The model is a heuristic synthesis intended to guide hypothesis generation; the small, literature-derived dataset and the illustrative nature of the calculations mean that all therapeutic suggestions are strictly indicative.

**Keywords:** blood–brain barrier, molecular descriptors, P-glycoprotein, membrane cross-sectional area, chameleonicity, local anesthetics

# 1. Introduction

The blood–brain barrier (BBB) is a specialized microvascular endothelium that limits the entry of most xenobiotics into the brain{{CITE:PARDIDGE2012}}. Medicinal chemists therefore need descriptors that predict whether a small molecule can cross this barrier. The most widely used guidelines are Lipinski's rule of five, developed to identify orally administered compounds with potential absorption problems, and the analogous CNS rules that emphasize moderate molecular weight, moderate lipophilicity, and low polar surface area{{CITE:LIPINSKI2001,RANKOVIC2015}}.

A critical point, however, is that such rules are guidelines, not guarantees. Lipinski's rule states that two or more violations are associated with poor oral absorption; it does not state that satisfying the rules ensures BBB permeability{{CITE:LIPINSKI2001}}. Likewise, CNS descriptors such as molecular weight below ~{{MW_CNS_MAX}} Da, cLogP between {{CNS_LOGP_MIN}} and {{CNS_LOGP_MAX}}, and total polar surface area below {{TPSA_CNS_MIN}}–{{TPSA_CNS_MAX}} Å² describe tendencies of successful CNS drugs but cannot certify that a compound will cross the BBB{{CITE:RANKOVIC2015}}.

Several well-known cases expose the limitations of a rule-of-five-only approach. Caffeine has a low logP (-0.07) yet readily enters the brain, whereas loperamide is highly lipophilic (logP 4.77) but is excluded from the CNS because it is a strong P-gp substrate{{CITE:SCHINKEL1996,CHEN2003}}. Morphine crosses the BBB only slowly, whereas its acetylated derivative heroin crosses far more rapidly despite a larger molecular weight and only a modestly higher logP{{CITE:XIE1999,FONG2015}}. Diazepam crosses well, whereas the larger and more lipophilic loratadine and cetirizine are kept out largely by P-gp-mediated efflux{{CITE:CHEN2003}}.

These paradoxes suggest that BBB permeability is governed by at least three partly independent gates: the cost of shedding the hydration shell (desolvation), the ability to partition into and diffuse through the lipid membrane (partition), and the balance between passive influx and active efflux (net flux){{CITE:FISCHER1998,FONG2015}}. In this paper we integrate these descriptors into a unified probabilistic model and discuss how the framework may inform the design of local anesthetics, micellar formulations, and metal-chelator therapies.

# 2. Approach and Methodology

## 2.1 Selection of Drugs

We compiled a literature-based dataset of {{N_DRUGS}} drugs: {{N_BBB_POS}} reported as BBB-permeable and {{N_BBB_NEG}} reported as BBB-poor (Table 1). The list was chosen because it contains classic CNS drugs as well as explicit counter-examples to simple logP/molecular-weight rules. Molecular weights (MW), logP values, hydrogen-bond donors (HBD), hydrogen-bond acceptors (HBA), and topological polar surface area (TPSA) were taken from public chemical databases and standard compilations.

## 2.2 Unconventional Descriptors Evaluated

We distinguished **conventional** descriptors—commonly found in quantitative structure–activity relationship (QSAR) models and derived from 2D/3D structure—from **unconventional** descriptors that capture membrane-specific or dynamic properties (Table 2).

### Unconventional descriptors

**Membrane cross-sectional area ($A_D$)** is the minimum area that a molecule presents when it inserts into a lipid bilayer. Fischer, Gottschlich and Seelig showed that compounds with $A_D < {{AD_LOW}}$ Å² cross most easily, values around {{AD_LOW}}–{{AD_CUTOFF}} Å² can cross, and values above ~{{AD_HIGH}} Å² are essentially excluded{{CITE:FISCHER1998,SEELIG1994PNAS,SEELIG2007}}. $A_D$ is related to, but not identical with, molecular weight: a flat, rigid molecule can have a small $A_D$ even at moderate MW.

**Collision cross-section (CCS)** is the rotationally averaged cross-section measured by ion-mobility mass spectrometry. Guntner and co-workers demonstrated that CCS separates BBB-penetrant from BBB-excluded compounds in larger datasets{{CITE:GUNTNER2019,GUNTNER2021}}. CCS provides experimental size/shape information that complements calculated $A_D$.

**P-gp net flux ($J_{\mathrm{net}}$)** is the difference between passive influx ($J_{\mathrm{influx}}$) and P-glycoprotein-mediated efflux ($J_{\mathrm{efflux}}$): $J_{\mathrm{net}} = J_{\mathrm{influx}} - J_{\mathrm{efflux}}$. Even molecules with favorable $A_D$ and desolvation can be excluded if they are strong P-gp substrates{{CITE:SCHINKEL1996,LINNET2008,ZHANG2012,LOSCHER2005}}.

**Chameleonicity / ΔPSA** describes the change in exposed polar surface area between aqueous and lipid environments. It is most powerful for macrocycles and beyond-Rule-of-Five compounds, which can bury polar groups through intramolecular hydrogen bonds in membranes{{CITE:POONGAVANAM2024,YU2026}}. Its contribution to classical small-molecule CNS drugs is limited because their polar surface areas are already small.

**Lateral bilayer pressure ($\pi_{bi}$)** is the mechanical pressure that a lipid bilayer exerts on an inserting molecule. Fischer and Seelig estimated $\pi_{bi} \approx {{PI_BI_MN_M}}\ \mathrm{mN/m}$ for BBB-mimicking membranes and derived the relationship

$$K_{lw} = \mathrm{const} \cdot K_{aw} \cdot \exp\left(-\frac{A_D \pi_{bi}}{kT}\right),$$

where $K_{lw}$ is the lipid–water partition coefficient, $K_{aw}$ is the air–water partition coefficient, $k$ is the Boltzmann constant, and $T$ is the absolute temperature{{CITE:FISCHER1998}}. This equation provides a physical rationale for why $A_D$ acts as an exponential filter.

**Substructural synergy** refers to the observation that certain combinations of fragments—such as aromatic rings, tertiary amines, and halogen atoms—appear together more often in BBB-penetrant molecules than would be expected from simple additive descriptors{{CITE:LEE2025}}. We treat this as a pattern descriptor, not as a mechanistic predictor.

### Conventional descriptors

**Molecular weight (MW)**, **logP**, **HBD**, **HBA**, and **TPSA** are the traditional Lipinski/CNS descriptors. We include them because they remain useful boundary conditions: for example, very polar, charged, or large molecules are generally BBB-excluded{{CITE:LIPINSKI2001,ABRAHAM2004}}.

**Dipole moment / polarizability** and **LUMO energy** are 3D electronic descriptors frequently used in QSAR studies{{CITE:MONTGOMERY2024,WANAT2023}}. They reflect electrostatic and polarizability effects on membrane interactions but, in this dataset, showed weaker independent discrimination than $A_D$ and P-gp status.

**3D-PSA** is a conformationally resolved version of polar surface area. It can improve over static TPSA when intramolecular hydrogen bonds shield polar groups{{CITE:SHITYAKOV2013}}.

{{TABLE1}}

## 2.3 Evaluation Criteria

Each factor was evaluated for: (a) BBB+/BBB- discriminatory power (ability to separate permeable from impermeable drugs); (b) independence from conventional descriptors (logP, MW, TPSA); (c) practical measurability; and (d) clinical utility. Ratings were assigned qualitatively and are reported in Table 2 and Figure 1.

{{TABLE2}}

## 2.4 Unified Model

We express the overall probability of BBB permeation as the product of three conditional probabilities:

$$P_{BBB} \propto P_{\mathrm{desolv}} \times P_{\mathrm{partition}} \times P_{\mathrm{net\,flux}}.$$

$P_{\mathrm{desolv}}$ is the probability that the molecule sheds its hydration shell rapidly enough to enter the membrane within the ~1 s capillary transit time; it depends on HBD number and strength, HBA, and charge{{CITE:FONG2015}}. $P_{\mathrm{partition}}$ is the probability of entering and diffusing through the lipid bilayer; it depends on $A_D$, $\pi_{bi}$, and lipophilicity{{CITE:FISCHER1998}}. $P_{\mathrm{net\,flux}}$ is the probability that passive influx exceeds P-gp (and other ABC transporter) efflux{{CITE:LINNET2008}}.

To illustrate the size dependence of $P_{\mathrm{partition}}$, we computed a relative partition term from the lateral bilayer pressure model:

$$P_{\mathrm{partition}}^{\mathrm{rel}}(A_D) = \exp\left[-\frac{\pi_{bi}}{kT}\left(A_D - A_{D,\mathrm{ref}}\right)\right],$$

with $A_{D,\mathrm{ref}} = {{A_REF}}$ Å² (ethanol, the smallest reference), $\pi_{bi} = {{PI_BI_MN_M}}\ \mathrm{mN/m} = {{PI_BI_N_M}}\ \mathrm{N/m}$, and $kT = {{KB}}\ \mathrm{J/K} \times {{TEMP_K}}\ \mathrm{K} = {{KT_J}}\ \mathrm{J}$. These values are normalized and are intended only to visualize the exponential relationship; they are not calibrated experimental permeabilities.

The therapeutic sections are presented as indicative, hypothesis-generating directions derived from the model, not as validated clinical recommendations.

# 3. Results

## 3.1 Factor Discriminatory Power

Figure 1 summarizes the discriminatory power of all descriptors. Membrane cross-sectional area ($A_D$) and P-gp net flux achieved the highest ratings, followed by desolvation energy, lateral bilayer pressure, 3D-PSA, and CCS. The conventional descriptors MW, logP, and TPSA remained useful boundary conditions but did not, by themselves, resolve the paradoxes noted in the Introduction.

{{FIGURE1}}

## 3.2 Drug × Factor Evaluation Matrix

Figure 2 presents the comprehensive evaluation matrix of all {{N_DRUGS}} drugs against the descriptors. BBB+ drugs consistently show favorable scores across the top-tier factors (A_D, net flux, desolvation), while BBB- drugs show unfavorable profiles in at least one critical factor.

{{FIGURE2}}

## 3.3 Membrane Cross-Sectional Area ($A_D$) as Primary Determinant

All BBB-positive drugs in the present dataset have estimated $A_D$ values below about {{AD_CUTOFF}} Å², whereas the BBB-negative drugs that are excluded by physical barriers have $A_D$ values at or above this range (Figure 3). Notably, this factor resolves the apparent paradox of caffeine (logP = -0.07, $A_D$ ~ 42 Å², BBB+) versus loperamide (logP = 4.77, $A_D$ ~ 90 Å², BBB-).

{{FIGURE3}}

## 3.4 Unified Three-Component Model

Based on the present analysis, BBB permeability can be modeled as the product of three sequential probabilities (Figure 4). $P_{\mathrm{desolv}}$ is the desolvation probability, $P_{\mathrm{partition}}$ is the membrane partition probability, and $P_{\mathrm{net\,flux}}$ is the net flux probability.

{{FIGURE4}}

## 3.5 Clinical Paradoxes Explained by the Unified Model

The model resolves several clinical paradoxes that conventional logP/MW-based models cannot explain (Figure 5, Table 3). Caffeine is small (MW < 200 Da) and has a very small $A_D$, so it can cross by paracellular or small-molecule diffusion even though its logP is low. Loperamide has a high logP but is a strong P-gp substrate and has $A_D$ > 80 Å², so its net flux is strongly negative. Heroin and codeine are derived from morphine but have fewer hydroxyl HBDs and therefore lower desolvation cost; the product $P_{BBB}$ is markedly higher for heroin than for morphine.

{{FIGURE5}}

{{TABLE3}}

# 4. Discussion

## 4.1 Re-interpreting Conventional and Unconventional Descriptors

The classification used here distinguishes conventional descriptors—MW, logP, TPSA, HBD, HBA, dipole moment/polarizability, LUMO energy, and 3D-PSA—from unconventional descriptors. The conventional set is derived directly from 2D or 3D structure and is commonly used in QSAR models{{CITE:LIPINSKI2001,WANAT2023,SHITYAKOV2013,MONTGOMERY2024}}. The unconventional set—$A_D$, CCS, P-gp net flux, chameleonicity/ΔPSA, lateral bilayer pressure, and substructural synergy—captures membrane-specific, dynamic, or transport-related behavior. The latter are included because they explain cases that conventional descriptors alone cannot.

The reference for lateral bilayer pressure is Fischer, Gottschlich and Seelig's 1998 study, which measured $\pi_{bi} \approx {{PI_BI_MN_M}}\ \mathrm{mN/m}$ and derived the exponential relationship between $A_D$ and membrane partitioning{{CITE:FISCHER1998}}. The reference for substructural synergy is Lee, Jun, Kim and colleagues' 2025 analysis of fragment combinations in BBB-penetrant molecules{{CITE:LEE2025}}.

## 4.2 Strengths and Limitations of the Unified Model

The three-gate model is a heuristic framework, not a fitted predictive equation. Its strength is conceptual: it links desolvation, membrane partitioning, and efflux into a single multiplicative probability and thereby explains caffeine, loperamide, morphine/heroin/codeine, diazepam, and the antihistamine pairs within one coherent picture.

The limitations must be emphasized. The dataset contains only {{N_DRUGS}} compounds, so any quantitative claim is tentative. Caffeine, ethanol, and nicotine are small enough that their permeability may be dominated by paracellular or small-molecule diffusion rather than lipid partitioning. L-DOPA and gabapentin are not passive diffusion cases; they cross via LAT1 or related transporters{{CITE:FONG2015}}. The descriptor values in Table 1 are estimated from published structures and reports, not measured in a single experimental series, so they should be treated as a curated synthesis rather than a validation dataset. The model also omits other transporters, plasma-protein binding, and metabolism.

## 4.3 Local Anesthetic Design

Local anesthetics are deliberately designed to produce peripheral nerve block with limited CNS entry. The model suggests that high $A_D$, high desolvation cost, or P-gp substrate status would reduce passive BBB permeation. Low BBB penetration, however, does not guarantee freedom from CNS side effects. Morphine illustrates this clearly: even with low BBB permeability, its high affinity for CNS opioid receptors means that the small fraction that does enter the brain is pharmacologically active{{CITE:XIE1999,RANKOVIC2015}}. A local anesthetic with similarly high CNS receptor affinity could produce unwanted central effects at low brain concentrations. Thus, the design suggestions here are indicative and must be combined with receptor-binding and toxicity data.

## 4.4 Micellar Formulation

Encapsulating a drug in micelles, liposomes, or other nanocarriers can change the rate-limiting step from passive transcellular diffusion to carrier release, endothelial uptake, or BBB disruption/receptor-mediated transport{{CITE:HU2025,MA2023}}. The unified model still applies, but the relevant descriptors become those of the drug–carrier system (size, surface charge, release kinetics, targeting ligand) rather than the free molecule. Because carrier design introduces additional variables, any BBB-penetration claim requires formulation-specific data; we therefore present this application as a conceptual direction.

## 4.5 Chelation-Based Effect Modification

Metal chelators such as deferoxamine (DFO) have mixed reports of BBB permeability. DFO is a relatively large, hydrophilic molecule, and systemic administration gives poor brain exposure; nevertheless, intranasal or encapsulated formulations can increase CNS delivery and have shown neuroprotective effects in preclinical models{{CITE:FARR2020}}. Chelation-based therapy therefore modifies the effective BBB penetration at the formulation/dosing level rather than by changing the intrinsic molecular descriptors. This application is also strictly indicative.

## 4.6 Relation to Broader Computational Efforts

Recent machine-learning studies that integrate multiple descriptors from standardized databases support the view that no single descriptor is sufficient for BBB prediction{{CITE:SPIELVOGEL2025}}. The unified model provides a mechanistic rationale for why such integrative approaches outperform single-parameter rules.

## 4.7 Translational Design Framework

The three-gate model can be summarized as a scaffold for the three indicative application areas discussed above (Figure 6). Micellar encapsulation changes the rate-limiting step from intrinsic membrane permeation to carrier release, endothelial uptake, or receptor-mediated targeting. Metal-chelator conjugates modify effective CNS exposure through formulation and route rather than by altering intrinsic molecular descriptors. Local-anesthetic optimization must balance membrane-exclusion descriptors, such as high $A_D$ or P-gp substrate status, against CNS receptor affinity, because very high affinity can produce central effects even at low brain concentrations. Because each application introduces variables outside the intrinsic descriptors, the framework is intended only as a conceptual guide, not as a validated design protocol.

{{FIGURE6}}

# 5. Conclusions

BBB permeability is better understood as the product of three gated probabilities—desolvation, membrane partition, and net transmembrane flux—than as a simple pass/fail rule. Membrane cross-sectional area and P-gp net flux provide the strongest discrimination in this small, literature-derived dataset, while desolvation cost and lateral bilayer pressure give physical explanations for several classic BBB paradoxes. The therapeutic applications to local anesthetics, micellar formulations, and chelation therapy are hypothesis-generating and require experimental validation. The present framework treats Lipinski/CNS rules as guidelines, clarifies the conventional versus unconventional descriptor classes, reports all descriptor values with references, and limits the clinical implications to hypothesis-generating directions.

# Figure Legends

**Figure 1.** Discriminatory power ranking of unconventional and conventional descriptors. Ratings are overall qualitative assessments based on the ability of each descriptor to separate BBB-permeable from BBB-poor compounds in the present dataset; see Table 2 for definitions and references.

**Figure 2.** Drug × factor evaluation matrix. Symbols: + favorable, o neutral, − weak, x unfavorable. Rows are ordered by BBB status (BBB+ drugs above the black line, BBB- drugs below). Columns correspond to the descriptors listed in Table 2. The matrix is intended as a visual summary of the dataset, not as a validated prediction model.

**Figure 3.** BBB permeability as a function of estimated membrane cross-sectional area ($A_D$). BBB+ drugs (green circles) have $A_D$ below about {{AD_CUTOFF}} Å²; BBB- drugs (red crosses) that are excluded by size have $A_D$ at or above this range. Vertical dashed lines indicate the {{AD_LOW}} Å², {{AD_CUTOFF}} Å², and {{AD_HIGH}} Å² boundaries from Fischer and Seelig.

**Figure 4.** Schematic representation of the unified three-component BBB permeability model. A molecule must pass three sequential gates—desolvation ($P_{\mathrm{desolv}}$), membrane partition ($P_{\mathrm{partition}}$), and net transmembrane flux ($P_{\mathrm{net\,flux}}$)—to reach brain parenchyma.

**Figure 5.** Unified model decomposition for six clinical cases. (A) Individual component probabilities estimated from the heuristic scoring rules described in Methods. (B) Product $P_{BBB}$ values. Green bars indicate BBB-permeable drugs; red bars indicate BBB-poor drugs. Values are relative and illustrative, not calibrated experimental permeabilities.

**Figure 6.** Conceptual framework for applying the unified BBB permeability model to drug-design strategies: micellar encapsulation, metal-chelator delivery, and local-anesthetic optimization. All three directions are indicative and require formulation-specific or receptor-binding data.

# References

{{REFERENCES}}
