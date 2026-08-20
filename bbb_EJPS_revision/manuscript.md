---
title: "Unconventional Molecular Descriptors for Blood–Brain Barrier Permeability Prediction: A Unified Model and Its Implications for Local Anesthetic Design, Micellar Formulation, and Chelation-Based Effect Modification"
author:
  - "Tatsuki Onishi"
  - "[Affiliation to be inserted]"
date: "19 August 2026"
abstract: |
  **Background.** Predicting blood–brain barrier (BBB) permeability remains a central problem in central nervous system (CNS) drug design. Conventional rules such as Lipinski's rule of five and related CNS guidelines describe physicochemical boundaries but do not guarantee permeability.
  **Objective.** We examined how ten molecular descriptors—including membrane cross-sectional area, collision cross-section, P-glycoprotein (P-gp) net flux, desolvation cost, chameleonicity, 3D polar surface area, dipole moment/polarizability, LUMO energy, substructural synergy, and lateral bilayer pressure—can be integrated into a single probabilistic framework.
  **Methods.** A curated set of 24 drugs (17 BBB-permeable, 7 BBB-poor) was compiled from the published literature. Descriptor values were estimated from public structural data, published binding/efflux data, and validated biophysical relationships; the relative membrane-partition term was calculated from the lateral bilayer pressure model.
  **Results.** Membrane cross-sectional area ($A_D$) and P-gp net flux discriminated BBB-positive from BBB-negative compounds most clearly. Desolvation cost distinguished morphine from heroin and codeine, and lateral bilayer pressure provided a physical rationale for the exponential size dependence of membrane partitioning. Caffeine, ethanol, and nicotine, all with molecular weight below 200 Da, are small enough to cross by paracellular or small-molecule diffusion, so their permeability does not rely solely on lipid-membrane partitioning.
  **Conclusions.** BBB permeability can be framed as the product of three gated probabilities: desolvation, membrane partition, and net transmembrane flux. The model is a heuristic synthesis intended to guide hypothesis generation; the small, literature-derived dataset and the illustrative nature of the calculations mean that all therapeutic suggestions are strictly indicative.
keywords: blood–brain barrier, molecular descriptors, P-glycoprotein, membrane cross-sectional area, chameleonicity, local anesthetics
---

# Introduction

The blood–brain barrier (BBB) is a specialized microvascular endothelium that limits the entry of most xenobiotics into the brain{{CITE:PARDIDGE2012}}. Medicinal chemists therefore need descriptors that predict whether a small molecule can cross this barrier. The most widely used guidelines are Lipinski's rule of five, developed to identify orally administered compounds with potential absorption problems, and the analogous CNS rules that emphasize moderate molecular weight, moderate lipophilicity, and low polar surface area{{CITE:LIPINSKI2001,RANKOVIC2015}}.

A critical point, however, is that such rules are guidelines, not guarantees. Lipinski's rule states that two or more violations are associated with poor oral absorption; it does not state that satisfying the rules ensures BBB permeability{{CITE:LIPINSKI2001}}. Likewise, CNS descriptors such as molecular weight below ~450 Da, cLogP between 1 and 3, and total polar surface area below 60–70 Å² describe tendencies of successful CNS drugs but cannot certify that a compound will cross the BBB{{CITE:RANKOVIC2015}}.

Several well-known cases expose the limitations of a rule-of-five-only approach. Caffeine has a low logP (-0.07) yet readily enters the brain, whereas loperamide is highly lipophilic (logP 4.77) but is excluded from the CNS because it is a strong P-gp substrate{{CITE:SCHINKEL1996,CHEN2003}}. Morphine crosses the BBB only slowly, whereas its acetylated derivative heroin crosses far more rapidly despite a larger molecular weight and only a modestly higher logP{{CITE:XIE1999,FONG2015}}. Diazepam crosses well, whereas the larger and more lipophilic loratadine and cetirizine are kept out largely by P-gp-mediated efflux{{CITE:CHEN2003}}.

These paradoxes suggest that BBB permeability is governed by at least three partly independent gates: the cost of shedding the hydration shell (desolvation), the ability to partition into and diffuse through the lipid membrane (partition), and the balance between passive influx and active efflux (net flux){{CITE:FISCHER1998,FONG2015}}. In this paper we integrate ten descriptors into a unified probabilistic model and discuss how the framework may inform the design of local anesthetics, micellar formulations, and metal-chelator therapies.

# Methods

## Dataset

We compiled a literature-based dataset of 24 drugs: 17 reported as BBB-permeable and 7 reported as BBB-poor (Table 1). The list was chosen because it contains classic CNS drugs as well as explicit counter-examples to simple logP/molecular-weight rules. Molecular weights (MW), logP values, hydrogen-bond donors (HBD), hydrogen-bond acceptors (HBA), and topological polar surface area (TPSA) were taken from public chemical databases and standard compilations.

## Descriptors and their classification

We distinguished **conventional** descriptors—commonly found in quantitative structure–activity relationship (QSAR) models and derived from 2D/3D structure—from **unconventional** descriptors that capture membrane-specific or dynamic properties (Table 2).

### Unconventional descriptors

**Membrane cross-sectional area ($A_D$)** is the minimum area that a molecule presents when it inserts into a lipid bilayer. Fischer, Gottschlich and Seelig showed that compounds with $A_D < 50$ Å² cross most easily, values around 50–70 Å² can cross, and values above ~80 Å² are essentially excluded{{CITE:FISCHER1998,SEELIG1994PNAS,SEELIG2007}}. $A_D$ is related to, but not identical with, molecular weight: a flat, rigid molecule can have a small $A_D$ even at moderate MW.

**Collision cross-section (CCS)** is the rotationally averaged cross-section measured by ion-mobility mass spectrometry. Guntner and co-workers demonstrated that CCS separates BBB-penetrant from BBB-excluded compounds in larger datasets{{CITE:GUNTNER2019,GUNTNER2021}}. CCS provides experimental size/shape information that complements calculated $A_D$.

**P-gp net flux ($J_{\mathrm{net}}$)** is the difference between passive influx ($J_{\mathrm{influx}}$) and P-glycoprotein-mediated efflux ($J_{\mathrm{efflux}}$): $J_{\mathrm{net}} = J_{\mathrm{influx}} - J_{\mathrm{efflux}}$. Even molecules with favorable $A_D$ and desolvation can be excluded if they are strong P-gp substrates{{CITE:SCHINKEL1996,LINNET2008,ZHANG2012,LOSCHER2005}}.

**Chameleonicity / ΔPSA** describes the change in exposed polar surface area between aqueous and lipid environments. It is most powerful for macrocycles and beyond-Rule-of-Five compounds, which can bury polar groups through intramolecular hydrogen bonds in membranes{{CITE:POONGAVANAM2024,YU2026}}. Its contribution to classical small-molecule CNS drugs is limited because their polar surface areas are already small.

**Lateral bilayer pressure ($\pi_{bi}$)** is the mechanical pressure that a lipid bilayer exerts on an inserting molecule. Fischer and Seelig estimated $\pi_{bi} \approx 34\ \mathrm{mN/m}$ for BBB-mimicking membranes and derived the relationship

$$K_{lw} = \mathrm{const} \cdot K_{aw} \cdot \exp\left(-\frac{A_D \pi_{bi}}{kT}\right),$$

where $K_{lw}$ is the lipid–water partition coefficient, $K_{aw}$ is the air–water partition coefficient, $k$ is the Boltzmann constant, and $T$ is the absolute temperature{{CITE:FISCHER1998}}. This equation provides a physical rationale for why $A_D$ acts as an exponential filter.

**Substructural synergy** refers to the observation that certain combinations of fragments—such as aromatic rings, tertiary amines, and halogen atoms—appear together more often in BBB-penetrant molecules than would be expected from simple additive descriptors{{CITE:LEE2025}}. We treat this as a pattern descriptor, not as a mechanistic predictor.

### Conventional descriptors

**Molecular weight (MW)**, **logP**, **HBD**, **HBA**, and **TPSA** are the traditional Lipinski/CNS descriptors. We include them because they remain useful boundary conditions: for example, very polar, charged, or large molecules are generally BBB-excluded{{CITE:LIPINSKI2001,ABRAHAM2004}}.

**Dipole moment / polarizability** and **LUMO energy** are 3D electronic descriptors frequently used in QSAR studies{{CITE:MONTGOMERY2024,WANAT2023}}. They reflect electrostatic and polarizability effects on membrane interactions but, in this dataset, showed weaker independent discrimination than $A_D$ and P-gp status.

**3D-PSA** is a conformationally resolved version of polar surface area. It can improve over static TPSA when intramolecular hydrogen bonds shield polar groups{{CITE:SHITYAKOV2013}}.

## Unified model

We express the overall probability of BBB permeation as the product of three conditional probabilities:

$$P_{BBB} \propto P_{\mathrm{desolv}} \times P_{\mathrm{partition}} \times P_{\mathrm{net\,flux}}.$$

$P_{\mathrm{desolv}}$ is the probability that the molecule sheds its hydration shell rapidly enough to enter the membrane within the ~1 s capillary transit time; it depends on HBD number and strength, HBA, and charge{{CITE:FONG2015}}. $P_{\mathrm{partition}}$ is the probability of entering and diffusing through the lipid bilayer; it depends on $A_D$, $\pi_{bi}$, and lipophilicity{{CITE:FISCHER1998}}. $P_{\mathrm{net\,flux}}$ is the probability that passive influx exceeds P-gp (and other ABC transporter) efflux{{CITE:LINNET2008}}.

To illustrate the size dependence of $P_{\mathrm{partition}}$, we computed a relative partition term from the lateral bilayer pressure model:

$$P_{\mathrm{partition}}^{\mathrm{rel}}(A_D) = \exp\left[-\frac{\pi_{bi}}{kT}\left(A_D - A_{D,\mathrm{ref}}\right)\right],$$

with $A_{D,\mathrm{ref}} = 20$ Å² (ethanol, the smallest reference), $\pi_{bi} = 34\ \mathrm{mN/m} = 0.034\ \mathrm{N/m}$, and $kT = 1.380\ 649 \times 10^{-23}\ \mathrm{J/K} \times 310\ \mathrm{K} = 4.278 \times 10^{-21}\ \mathrm{J}$. These values are normalized and are intended only to visualize the exponential relationship; they are not calibrated experimental permeabilities.

## Applications

The therapeutic sections are presented as indicative, hypothesis-generating directions derived from the model, not as validated clinical recommendations.

# Results

{{TABLE1}}

Table 1 reports the descriptor values and the key literature sources for the 24 drugs. Figure 1 presents the unified three-gate model schematically, and Figure 2 shows the estimated $A_D$ values and the corresponding relative partition term for each compound.

{{FIGURE1}}

{{FIGURE2}}

Two descriptors dominate the separation between BBB-permeable and BBB-poor compounds. First, all BBB-positive drugs have estimated $A_D$ values below about 70 Å², whereas the BBB-negative drugs that are excluded by size (loratadine, cetirizine, loperamide, doxorubicin, vincristine, atenolol) have $A_D$ values at or above this range. Second, P-gp substrate status explains several otherwise paradoxical cases: loperamide is highly lipophilic but is a strong P-gp substrate; loratadine and cetirizine are second-generation antihistamines whose P-gp-mediated efflux limits CNS entry{{CITE:SCHINKEL1996,CHEN2003,LINNET2008}}.

Caffeine, ethanol, and nicotine have molecular weights below 200 Da. Their BBB entry is consistent with paracellular and small-molecule diffusion pathways, not with a requirement for high lipophilicity or large membrane-partition coefficients{{CITE:ABRAHAM2004,PARDIDGE2012}}. Therefore, their inclusion does not imply that they satisfy a conventional Lipinski/CNS rule; rather, they illustrate that very small molecules can bypass some of the lipid-membrane barriers.

Desolvation cost distinguishes morphine from heroin and codeine. Morphine has two hydroxyl groups (HBD = 2), a rigid pentacyclic scaffold, and a measurable P-gp efflux component; these features give it low but non-zero BBB permeability{{CITE:XIE1999,FONG2015}}. Acetylation of morphine to heroin removes the hydroxyl HBDs, lowers desolvation cost, and markedly increases BBB permeability despite an increase in molecular weight{{CITE:FONG2015}}. Methylation to codeine is intermediate.

Diazepam represents a near-optimal combination: small $A_D$, no HBD, non-P-gp substrate, and a planar benzodiazepine scaffold. Chlorpromazine and haloperidol also cross, but their larger $A_D$ places them closer to the cutoff.

{{TABLE2}}

Table 2 summarizes the conventional/unconventional classification and our assessment of discriminatory utility for each descriptor.

# Discussion

## Re-interpreting conventional and unconventional descriptors

The classification used here distinguishes conventional descriptors—MW, logP, TPSA, HBD, HBA, dipole moment/polarizability, LUMO energy, and 3D-PSA—from unconventional descriptors. The conventional set is derived directly from 2D or 3D structure and is commonly used in QSAR models{{CITE:LIPINSKI2001,WANAT2023,SHITYAKOV2013,MONTGOMERY2024}}. The unconventional set—$A_D$, CCS, P-gp net flux, chameleonicity/ΔPSA, lateral bilayer pressure, and substructural synergy—captures membrane-specific, dynamic, or transport-related behavior. The latter are included because they explain cases that conventional descriptors alone cannot.

The reference for lateral bilayer pressure is Fischer, Gottschlich and Seelig's 1998 study, which measured $\pi_{bi} \approx 34\ \mathrm{mN/m}$ and derived the exponential relationship between $A_D$ and membrane partitioning{{CITE:FISCHER1998}}. The reference for substructural synergy is Lee, Jun, Kim and colleagues' 2025 analysis of fragment combinations in BBB-permeable molecules{{CITE:LEE2025}}.

## Strengths and limitations of the unified model

The three-gate model is a heuristic framework, not a fitted predictive equation. Its strength is conceptual: it links desolvation, membrane partitioning, and efflux into a single multiplicative probability and thereby explains caffeine, loperamide, morphine/heroin/codeine, diazepam, and the antihistamine pairs within one coherent picture.

The limitations must be emphasized. The dataset contains only 24 compounds, so any quantitative claim is tentative. Caffeine, ethanol, and nicotine are small enough that their permeability may be dominated by paracellular or small-molecule diffusion rather than lipid partitioning. L-DOPA and gabapentin are not passive diffusion cases; they cross via LAT1 or related transporters{{CITE:FONG2015}}. The descriptor values in Table 1 are estimated from published structures and reports, not measured in a single experimental series, so they should be treated as a curated synthesis rather than a validation dataset. The model also omits other transporters, plasma-protein binding, and metabolism.

## Local anesthetic design

Local anesthetics are deliberately designed to produce peripheral nerve block with limited CNS entry. The model suggests that high $A_D$, high desolvation cost, or P-gp substrate status would reduce passive BBB permeation. Low BBB penetration, however, does not guarantee freedom from CNS side effects. Morphine illustrates this clearly: even with low BBB permeability, its high affinity for CNS opioid receptors means that the small fraction that does enter the brain is pharmacologically active{{CITE:XIE1999,RANKOVIC2015}}. A local anesthetic with similarly high CNS receptor affinity could produce unwanted central effects at low brain concentrations. Thus, the design suggestions here are indicative and must be combined with receptor-binding and toxicity data.

## Micellar formulation

Encapsulating a drug in micelles, liposomes, or other nanocarriers can change the rate-limiting step from passive transcellular diffusion to carrier release, endothelial uptake, or BBB disruption/receptor-mediated transport{{CITE:HU2025,MA2023}}. The unified model still applies, but the relevant descriptors become those of the drug–carrier system (size, surface charge, release kinetics, targeting ligand) rather than the free molecule. Because carrier design introduces additional variables, any BBB-penetration claim requires formulation-specific data; we therefore present this application as a conceptual direction.

## Chelation-based effect modification

Metal chelators such as deferoxamine (DFO) have mixed reports of BBB permeability. DFO is a relatively large, hydrophilic molecule, and systemic administration gives poor brain exposure; nevertheless, intranasal or encapsulated formulations can increase CNS delivery and have shown neuroprotective effects in preclinical models{{CITE:FARR2020}}. Chelation-based therapy therefore modifies the effective BBB penetration at the formulation/dosing level rather than by changing the intrinsic molecular descriptors. This application is also strictly indicative.

## Relation to broader computational efforts

Recent machine-learning studies that integrate multiple descriptors from standardized databases support the view that no single descriptor is sufficient for BBB prediction{{CITE:SPIELVOGEL2025}}. The unified model provides a mechanistic rationale for why such integrative approaches outperform single-parameter rules.

# Conclusion

BBB permeability is better understood as the product of three gated probabilities—desolvation, membrane partition, and net transmembrane flux—than as a simple pass/fail rule. Membrane cross-sectional area and P-gp net flux provide the strongest discrimination in this small, literature-derived dataset, while desolvation cost and lateral bilayer pressure give physical explanations for several classic BBB paradoxes. The therapeutic applications to local anesthetics, micellar formulations, and chelation therapy are hypothesis-generating and require experimental validation. The present framework treats Lipinski/CNS rules as guidelines, clarifies the conventional versus unconventional descriptor classes, reports all descriptor values with references, and limits the clinical implications to hypothesis-generating directions.

# Figure legends

**Figure 1.** The unified three-gate model of BBB permeability. A molecule must first shed its hydration shell ($P_{\mathrm{desolv}}$), then partition into and diffuse through the lipid bilayer ($P_{\mathrm{partition}}$), and finally reach a positive net flux across the endothelial layer ($P_{\mathrm{net\,flux}} = J_{\mathrm{influx}} - J_{\mathrm{efflux}}$). $A_D$ = membrane cross-sectional area; $\pi_{bi}$ = lateral bilayer pressure; P-gp = P-glycoprotein.

**Figure 2.** Estimated membrane cross-sectional area ($A_D$) and the corresponding relative partition term, $P_{\mathrm{partition}}^{\mathrm{rel}}$, computed from the lateral bilayer pressure model for the 24 drugs. BBB-permeable compounds are shown in blue, BBB-poor compounds in orange. The dashed line marks the $A_D \approx 70$ Å² cutoff above which membrane partitioning drops sharply.

# References

{{REFERENCES}}
