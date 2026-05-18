# 血液脳関門（BBB）通過薬剤・超音波技術・分子振動数に関する調査レポート

## 1. BBBを通過できることが知られている薬剤のリスト

### 1.1 受動拡散（Passive Diffusion）で通過する薬剤

BBBを受動拡散で通過する薬剤の一般的な特徴（Pardridge, 2012; Banks, 2009）:
- **分子量**: < 400 Da
- **水素結合数**: < 8個
- **脂溶性（logP）**: 高い（ただし高すぎると末梢組織に捕捉される）
- **PSA（極性表面積）**: < 90 Å²

CNS薬に特化した「Lipinski's Rule for CNS drugs (RoCNS)」（Lipinski, 1999）:
- HBD（水素結合ドナー）≤ 3
- HBA（水素結合アクセプター）≤ 7
- MW ≤ 400 Da
- CLogP ≤ 5

| 薬剤名 | 分類 | 分子量 (Da) | logP (概算) | 通過メカニズム |
|---|---|---|---|---|
| **カフェイン** (Caffeine) | 精神刺激薬 | 194.2 | -0.07 | 受動拡散 |
| **エタノール** (Ethanol) | アルコール | 46.1 | -0.31 | 受動拡散 |
| **ニコチン** (Nicotine) | 刺激薬 | 162.2 | 1.17 | 受動拡散 |
| **ジアゼパム** (Diazepam/Valium) | ベンゾジアゼピン | 284.7 | 2.82 | 受動拡散 |
| **モルヒネ** (Morphine) | オピオイド | 285.3 | 0.89 | 受動拡散（低透過性） |
| **ヘロイン** (Diacetylmorphine) | オピオイド | 369.4 | 1.58 | 受動拡散（高脂溶性） |
| **コデイン** (Codeine) | オピオイド | 299.4 | 1.19 | 受動拡散 |
| **プロポフォール** (Propofol) | 全身麻酔薬 | 178.3 | 3.79 | 受動拡散 |
| **フルオキセチン** (Fluoxetine/Prozac) | SSRI | 309.3 | 4.05 | 受動拡散 |
| **ジフェンヒドラミン** (Diphenhydramine) | 第1世代抗ヒスタミン薬 | 255.4 | 3.27 | 受動拡散 |
| **フェノバルビタール** (Phenobarbital) | バルビツール酸系 | 232.2 | 1.47 | 受動拡散 |
| **カルバマゼピン** (Carbamazepine) | 抗てんかん薬 | 236.3 | 2.45 | 受動拡散 |
| **フェニトイン** (Phenytoin) | 抗てんかん薬 | 252.3 | 2.47 | 受動拡散 |
| **クロルプロマジン** (Chlorpromazine) | 抗精神病薬 | 318.9 | 5.41 | 受動拡散 |
| **ハロペリドール** (Haloperidol) | 抗精神病薬 | 375.9 | 4.3 | 受動拡散 |
| **イブプロフェン** (Ibuprofen) | NSAID | 206.3 | 3.97 | 受動拡散（限定的） |

### 1.2 トランスポーター介在輸送で通過する薬剤

| 薬剤名 | 分類 | 分子量 (Da) | トランスポーター |
|---|---|---|---|
| **L-DOPA** (レボドパ) | パーキンソン治療薬 | 197.2 | LAT1（大型中性アミノ酸トランスポーター） |
| **ガバペンチン** (Gabapentin) | 抗てんかん薬 | 171.2 | LAT1 |
| **メルファラン** (Melphalan) | 抗がん剤 | 305.2 | LAT1 |
| **グルコース** | 栄養素 | 180.2 | GLUT1 |

### 1.3 BBBを通過しにくい薬剤（参考）

| 薬剤名 | 理由 |
|---|---|
| ドーパミン | 極性が高い、トランスポーターなし |
| ロラタジン（第2世代抗ヒスタミン） | P-glycoproteinによる排出 |
| ほとんどの抗体医薬 | 分子量 > 150,000 Da |
| 多くの化学療法薬 | 分子量過大、P-gp基質 |

---

## 2. 超音波照射によるBBB一時的開放技術（FUS-BBBO）

### 2.1 技術の概要

**Focused Ultrasound Blood-Brain Barrier Opening (FUS-BBBO)** は、集束超音波（Focused Ultrasound, FUS）と静脈内投与されたマイクロバブル（微小気泡）を組み合わせて、BBBを一時的かつ局所的に開放する技術である。

### 2.2 使用される超音波パラメータ

| パラメータ | 典型値 | 備考 |
|---|---|---|
| **超音波周波数** | **200 kHz 〜 1.5 MHz** | 臨床ではExAblate Neuro: 220 kHz, NaviFUS: 500 kHz |
| **音響圧** | 150〜750 kPa | 安全域: 450 kPa以下（Nature 2026） |
| **Mechanical Index (MI)** | 0.3〜0.8 | 安全域: MI ≤ 0.55 |
| **パルスモード** | バーストモード | 連続波ではなくパルス照射 |
| **パルス繰り返し周波数** | 1〜10 Hz | |
| **照射時間** | 数十秒〜数分 | |
| **マイクロバブル** | 直径 1〜10 μm | Definity, SonoVue等 |

**周波数の換算**:
- 200 kHz = 2 × 10⁵ Hz
- 500 kHz = 5 × 10⁵ Hz  
- 1 MHz = 1 × 10⁶ Hz

### 2.3 メカニズム

FUS-BBBOのメカニズムは以下の通り（Nature Communications Engineering, 2026; Tung et al., 2011）:

1. **マイクロバブルの注入**: 脂質殻で覆われた微小気泡を静脈内投与
2. **超音波照射**: 集束超音波が脳の標的領域に照射される
3. **キャビテーション（空洞化）**: 
   - **安定キャビテーション（Stable cavitation）**: マイクロバブルが超音波場で振動し、血管壁に機械的応力を与える
   - **慣性キャビテーション（Inertial cavitation）**: 高圧下でバブルが崩壊し、衝撃波を生成（損傷リスクあり）
4. **タイトジャンクションの一時的再編成**: 
   - 低圧（450 kPa）: タイトジャンクション蛋白（claudin-5等）の**一時的な再編成と修復**
   - 高圧（750 kPa）: タイトジャンクションの**破壊**（72時間後も未修復）
5. **BBB透過性の増加**: 通常通過できない薬剤が脳実質に到達可能に
6. **自然回復**: 低圧照射の場合、数時間〜24時間以内にBBBが回復

### 2.4 重要な知見（最新研究）

- **2026年 Nature Communications Engineering**: BBB開放のメカニズムはタイトジャンクションの一時的再編成が主因であり、カベオラ（caveolae）依存ではない
- FUS-BBBOの臨床試験が進行中：アルツハイマー病、脳腫瘍（GBM）、パーキンソン病
- 超音波はマイクロバブルを介した**マクロスケールの機械的作用**であり、分子レベルの共鳴ではない

---

## 3. BBB通過薬剤の分子振動数

### 3.1 分子振動の基礎知識

分子振動は分子内の原子が周期的に運動する現象で、以下の周波数帯域に分類される：

| 振動の種類 | 周波数範囲 | 波数 (cm⁻¹) | 備考 |
|---|---|---|---|
| **分子内振動（Mid-IR）** | 10¹³〜10¹⁴ Hz (10〜100 THz) | 400〜4000 cm⁻¹ | C-H, O-H, N-H伸縮、C=O伸縮等 |
| **低周波振動（THz/Far-IR）** | 10¹¹〜10¹³ Hz (0.1〜10 THz) | 3〜333 cm⁻¹ | 格子振動、分子間振動、骨格変形 |
| **マイクロ波領域** | 10⁹〜10¹¹ Hz (1〜100 GHz) | | 分子回転 |

### 3.2 各薬剤の代表的振動モード（IR/Raman）

#### カフェイン (Caffeine, MW=194.2)
- C=O伸縮: ~1700 cm⁻¹ (~51 THz)
- C=N伸縮: ~1600 cm⁻¹ (~48 THz)
- C-N伸縮: ~1200-1400 cm⁻¹ (~36-42 THz)
- CH₃変形: ~1450 cm⁻¹ (~43 THz)
- THz領域（格子振動）: 0.5〜3 THz（NISTデータベース）

#### ジアゼパム (Diazepam, MW=284.7)
- C=O伸縮: ~1690 cm⁻¹ (~50.7 THz)
- C=N伸縮（ジアゼピン環）: ~1610 cm⁻¹ (~48.3 THz, Raman)
- 芳香環C=C伸縮: ~1580-1600 cm⁻¹
- C-Cl伸縮: ~750 cm⁻¹ (~22.5 THz)
- ベンゾジアゼピン骨格: 400-900 cm⁻¹

#### モルヒネ (Morphine, MW=285.3)
- O-H伸縮: ~3300-3500 cm⁻¹ (~99-105 THz)
- 芳香環C-H伸縮: ~3050 cm⁻¹
- C=C伸縮: ~1600 cm⁻¹
- C-O伸縮: ~1050-1250 cm⁻¹
- 低周波モード: Raman研究により多数の振動バンドが確認 (Baranska, 2012)

#### エタノール (Ethanol, MW=46.1)
- O-H伸縮: ~3300 cm⁻¹ (~99 THz)
- C-H伸縮: ~2900 cm⁻¹ (~87 THz)
- C-O伸縮: ~1050 cm⁻¹ (~31.5 THz)
- C-C伸縮: ~880 cm⁻¹ (~26.4 THz)

#### プロポフォール (Propofol, MW=178.3)
- O-H伸縮: ~3600 cm⁻¹
- 芳香環C=C伸縮: ~1600 cm⁻¹
- C-H変形: ~1460 cm⁻¹
- フェノールC-O伸縮: ~1200 cm⁻¹

### 3.3 BBB通過薬剤の振動特性の共通点

BBB通過薬剤に共通するIR/Raman振動バンド：

| 官能基/振動モード | 波数範囲 (cm⁻¹) | 周波数 (THz) | 出現頻度 |
|---|---|---|---|
| C-H伸縮 | 2800-3100 | 84-93 | ほぼ全薬剤 |
| 芳香環C=C伸縮 | 1580-1610 | 47-48 | 多くの薬剤 |
| C=O伸縮 | 1650-1700 | 49-51 | バルビツール酸系、ベンゾジアゼピン系 |
| C-N伸縮 | 1200-1400 | 36-42 | 含窒素化合物 |
| C-O伸縮 | 1000-1250 | 30-37 | 多くの薬剤 |

**重要**: これらの振動モードは分子の官能基に依存するため、BBB通過薬剤に特有ではない。BBBを通過しない薬剤も同じ官能基を持つ場合、同様の振動数を示す。

---

## 4. 仮説の検証：分子振動数と超音波によるBBB開放の関連性

### 4.1 仮説の整理

> 「BBB通過薬剤の分子振動数に共通する特徴があり、超音波によるBBB開放技術は、この振動数に関連した原理で薬剤を通過させている」

### 4.2 周波数スケールの比較（最重要ポイント）

| カテゴリ | 周波数 | Hz表記 | 備考 |
|---|---|---|---|
| **FUS-BBBO超音波** | 200 kHz〜1.5 MHz | 2×10⁵ 〜 1.5×10⁶ Hz | マクロ機械的作用 |
| **分子内振動（Mid-IR）** | 10〜100 THz | 10¹³ 〜 10¹⁴ Hz | C-H, C=O等の結合振動 |
| **低周波分子振動（THz）** | 0.1〜10 THz | 10¹¹ 〜 10¹³ Hz | 格子振動、分子間力 |

**周波数の差**: 超音波（~10⁵〜10⁶ Hz）と分子振動（~10¹¹〜10¹⁴ Hz）の間には **約5〜9桁（10万倍〜10億倍）の差** がある。

### 4.3 仮説に対する科学的評価

#### 仮説を支持しない根拠

1. **周波数スケールの根本的不一致**:
   - 超音波（kHz〜MHz）と分子振動（THz〜数十THz）では周波数が5〜9桁異なる
   - 共鳴現象が起こるには周波数の一致が必要であり、これほどの差では分子共鳴は物理的に不可能
   - 例: カフェインのC=O伸縮振動 (~51 THz) に共鳴させるには51 THzの電磁波が必要であり、500 kHzの超音波では全く異なる物理領域

2. **FUS-BBBOのメカニズムは機械的作用**:
   - 超音波はマイクロバブルの膨張・収縮（キャビテーション）を誘発
   - バブルの振動が血管壁に物理的な機械的応力（shear stress）を生じさせる
   - タイトジャンクション蛋白質が一時的に再編成される（2026年Nature論文で確認）
   - これは**分子レベルの共鳴ではなく、細胞・組織レベルの機械的破壊と修復**

3. **BBB通過の古典的メカニズムとの矛盾**:
   - 受動拡散によるBBB通過は、分子量・脂溶性・水素結合数で予測可能
   - 超音波は「通過できない薬剤を通過させる」技術であり、「もともと通過できる薬剤の特性」とは異なる原理
   - 超音波BBB開放後は、分子量数万Daの抗体ですら通過可能になる（振動特性とは無関係）

4. **振動数はBBB通過の選択性を説明しない**:
   - 同じ官能基（C=O, C-H等）を持つ薬剤でも、BBBを通過するものとしないものがある
   - 例: モルヒネ（BBB通過あり、logP=0.89）とペニシリンG（BBB通過なし、logP=1.83）は類似の振動バンドを持つが、BBB透過性は大きく異なる

#### 仮説の興味深い側面

ただし、以下の点は今後の研究に値する可能性がある：

1. **超音波による分子の機械化学的活性化（Sonopharmacology）**:
   - 超音波がポリマー鎖の機械的破断を引き起こし、薬剤を放出する技術は存在する
   - ただしこれは共有結合の破断であり、分子振動との共鳴ではない

2. **低周波集団振動モード**:
   - 蛋白質やDNAにはGHz帯域の集団振動モードが存在する
   - 理論的には超音波（MHz）とこれらの低周波モードの高調波が相互作用する可能性はゼロではないが、実験的証拠は現時点で存在しない

3. **音響放射力（Acoustic Radiation Force）による分子輸送**:
   - 超音波は分子に直接的な放射力を及ぼすことで輸送を促進し得る
   - この効果は分子の音響インピーダンスに依存し、振動モードとは別の物理量

---

## 5. 結論

### 現在の科学的コンセンサスに基づく評価

| 項目 | 結論 |
|---|---|
| BBB通過薬剤の共通特徴 | 分子量 < 400 Da、高脂溶性、少ない水素結合（振動数ではなく物理化学的性質） |
| FUS-BBBOのメカニズム | マイクロバブルキャビテーションによる機械的タイトジャンクション再編成 |
| 分子振動と超音波の関連 | **周波数スケールが5〜9桁異なり、直接的な共鳴メカニズムは物理的に成立しない** |

### 仮説の修正提案

もし振動に関連する仮説を追求するのであれば、以下の方向性がより科学的に妥当と考えられます：

1. **タイトジャンクション蛋白質の集団振動モード（GHz帯域）と超音波の相互作用**: claudin-5等のタイトジャンクション蛋白質が特定の低周波振動モードを持ち、超音波がこれらに影響を与える可能性を調べる

2. **脂質二重膜の振動特性と薬剤分子の膜透過性の関係**: BBB内皮細胞の脂質膜が特定の振動モードを持ち、通過しやすい薬剤がこの膜振動と適合する動的特性を持つかどうか

3. **音響キャビテーションによるナノスケール流体力学**: バブル崩壊時の局所的な流れが薬剤分子のサイズ・形状に依存した選択的輸送を可能にするか

---

## 参考文献

1. Pardridge WM. Drug transport across the blood-brain barrier. *J Cereb Blood Flow Metab*. 2012;32(11):1959-1972.
2. Banks WA. Characteristics of compounds that cross the blood-brain barrier. *BMC Neurol*. 2009;9(Suppl 1):S3.
3. Pajouhesh H, Lenz GR. Medicinal Chemical Properties of Successful CNS Drugs. *NeuroRx*. 2005;2(4):541-553.
4. Konofagou EE et al. Safe focused ultrasound-mediated blood-brain barrier opening is driven primarily by transient reorganization of tight junctions. *Commun Eng*. 2026.
5. Tung YS et al. The mechanism of interaction between focused ultrasound and microbubbles in blood-brain barrier opening in mice. *J Acoust Soc Am*. 2011;130(5):3059-3067.
6. Chen H, Konofagou EE. The size of blood-brain barrier opening induced by focused ultrasound is dictated by the acoustic pressure. *J Cereb Blood Flow Metab*. 2014;34(7):1197-1204.
7. Baranska M. Morphine studied by vibrational spectroscopy and DFT calculations. *J Raman Spectrosc*. 2012;43(1):102-107.
8. Neville GA et al. Fourier transform Raman and infrared vibrational study of diazepam and related 1,4-benzodiazepines. *J Raman Spectrosc*. 1990;21(1):9-19.
9. Yildiz D, Göstl R, Herrmann A. Sonopharmacology: controlling pharmacotherapy by ultrasound-induced polymer mechanochemistry. *Chem Sci*. 2022.
10. Fernandes TB et al. Analysis of the Applicability and Use of Lipinski's Rule for CNS Drugs. *Lett Drug Des Discov*. 2016;13(10):999-1006.

---

# English Translation

---

# Research report on drugs that cross the blood-brain barrier (BBB), ultrasound technology, and molecular frequencies

## 1. List of drugs known to be able to cross the BBB

### 1.1 Drugs passing by passive diffusion

General characteristics of drugs that pass through the BBB by passive diffusion (Pardridge, 2012; Banks, 2009):
- **Molecular weight**: < 400 Da
- **Number of hydrogen bonds**: < 8
- **Lipid solubility (logP)**: High (but if it is too high, it will be trapped in peripheral tissues)
- **PSA (Polar Surface Area)**: < 90 Å²

"Lipinski's Rule for CNS drugs (RoCNS)" (Lipinski, 1999):
- HBD (hydrogen bond donor) ≤ 3
- HBA (hydrogen bond acceptor) ≤ 7
- MW ≤ 400 Da
- CLogP ≤ 5

| Drug name | Classification | Molecular weight (Da) | logP (approximate) | Passage mechanism |
|---|---|---|---|---|
| **Caffeine** (Caffeine) | Psychostimulant | 194.2 | -0.07 | Passive Diffusion |
| **Ethanol** (Ethanol) | Alcohol | 46.1 | -0.31 | Passive Diffusion |
| **Nicotine** (Nicotine) | Stimulant | 162.2 | 1.17 | Passive Diffusion |
| **Diazepam** (Diazepam/Valium) | Benzodiazepines | 284.7 | 2.82 | Passive Diffusion |
| **morphine** (Morphine) | Opioids | 285.3 | 0.89 | Passive diffusion (low permeability) |
| **Heroin** (Diacetylmorphine) | Opioids | 369.4 | 1.58 | Passive diffusion (high lipid solubility) |
| **Codeine** (Codeine) | Opioids | 299.4 | 1.19 | Passive Diffusion |
| **Propofol** (Propofol) | General Anesthetic | 178.3 | 3.79 | Passive Diffusion |
| **Fluoxetine** (Fluoxetine/Prozac) | SSRI | 309.3 | 4.05 | Passive Diffusion |
| **Diphenhydramine** (Diphenhydramine) | First generation antihistamine | 255.4 | 3.27 | Passive diffusion |
| **Phenobarbital** (Phenobarbital) | Barbiturates | 232.2 | 1.47 | Passive Diffusion |
| **Carbamazepine** (Carbamazepine) | Antiepileptic drug | 236.3 | 2.45 | Passive diffusion |
| **Phenytoin** (Phenytoin) | Antiepileptic drugs | 252.3 | 2.47 | Passive diffusion |
| **Chlorpromazine** (Chlorpromazine) | Antipsychotics | 318.9 | 5.41 | Passive Diffusion |
| **Haloperidol** (Haloperidol) | Antipsychotics | 375.9 | 4.3 | Passive Diffusion |
| **Ibuprofen** (Ibuprofen) | NSAID | 206.3 | 3.97 | Passive Diffusion (Limited) |

### 1.2 Drugs passing through transporter-mediated transport

| Drug name | Classification | Molecular weight (Da) | Transporter |
|---|---|---|---|
| **L-DOPA** (Levodopa) | Parkinson's treatment | 197.2 | LAT1 (Large neutral amino acid transporter) |
| **Gabapentin** (Gabapentin) | Antiepileptic drug | 171.2 | LAT1 |
| **Melphalan** (Melphalan) | Anticancer drug | 305.2 | LAT1 |
| **Glucose** | Nutrients | 180.2 | GLUT1 |
### 1.3 Drugs that do not easily cross the BBB (reference)

| Drug name | Reason |
|---|---|
| Dopamine | Highly polar, no transporter |
| Loratadine (2nd generation antihistamine) | Excretion by P-glycoprotein |
| Most antibody drugs | Molecular weight > 150,000 Da |
| Many chemotherapy drugs | Excessive molecular weight, P-gp substrate |

---

## 2. BBB temporary opening technology using ultrasound irradiation (FUS-BBBO)

### 2.1 Technology overview

**Focused Ultrasound Blood-Brain Barrier Opening (FUS-BBBO)** is a technology that combines focused ultrasound (FUS) and intravenously administered microbubbles to temporarily and locally open the BBB.

### 2.2 Ultrasonic parameters used

| Parameter | Typical value | Notes |
|---|---|---|
| **Ultrasound Frequency** | **200 kHz to 1.5 MHz** | Clinically ExAblate Neuro: 220 kHz, NaviFUS: 500 kHz |
| **Sound pressure** | 150 to 750 kPa | Safety margin: 450 kPa or less (Nature 2026) |
| **Mechanical Index (MI)** | 0.3~0.8 | Safety margin: MI ≤ 0.55 |
| **Pulse mode** | Burst mode | Pulse irradiation instead of continuous wave |
| **Pulse repetition frequency** | 1~10 Hz | |
| **Irradiation time** | Several tens of seconds to several minutes | |
| **Microbubbles** | Diameter 1-10 μm | Definity, SonoVue, etc. |

**Frequency conversion**:
- 200 kHz = 2 × 10⁵ Hz
- 500 kHz = 5 × 10⁵ Hz
- 1 MHz = 1 × 10⁶ Hz

### 2.3 Mechanism

The mechanism of FUS-BBBO is as follows (Nature Communications Engineering, 2026; Tung et al., 2011):

1. **Microbubble injection**: Intravenous administration of microbubbles covered with a lipid shell
2. **Ultrasound irradiation**: Focused ultrasound waves are applied to targeted areas of the brain.
3. **Cavitation**:
   - **Stable cavitation**: Microbubbles vibrate in an ultrasound field and exert mechanical stress on the blood vessel wall
- **Inertial cavitation**: bubble collapses under high pressure, creating shock waves (risk of damage)
4. **Temporary reorganization of tight junctions**:
   - Low pressure (450 kPa): **Temporary reorganization and repair of tight junction proteins (such as claudin-5)**
   - High pressure (750 kPa): **destruction** of tight junctions (unrepaired after 72 hours)
5. **Increased BBB permeability**: Drugs that normally cannot pass through can now reach the brain parenchyma.
6. **Spontaneous recovery**: In the case of low-pressure irradiation, the BBB recovers within a few hours to 24 hours.

### 2.4 Important findings (latest research)

- **2026 Nature Communications Engineering**: The mechanism of BBB opening is mainly caused by temporary reorganization of tight junctions and is not dependent on caveolae.
- FUS-BBBO clinical trials underway: Alzheimer's disease, brain tumor (GBM), Parkinson's disease
- Ultrasound is a **macroscale mechanical action** via microbubbles, not resonance at the molecular level.

---

## 3. Molecular frequencies of drugs passing through the BBB

### 3.1 Basic knowledge of molecular vibrations

Molecular vibration is a phenomenon in which atoms within a molecule move periodically and is classified into the following frequency bands:
| Type of vibration | Frequency range | Wave number (cm⁻¹) | Notes |
|---|---|---|---|
| **Intramolecular vibration (Mid-IR)** | 10¹³～10¹⁴ Hz (10～100 THz) | 400～4000 cm⁻¹ | C-H, O-H, N-H stretching, C=O stretching, etc. |
| **Low frequency vibration (THz/Far-IR)** | 10¹¹~10¹³ Hz (0.1~10 THz) | 3~333 cm⁻¹ | Lattice vibration, intermolecular vibration, skeletal deformation |
| **Microwave region** | 10⁹~10¹¹ Hz (1~100 GHz) | | Molecular rotation |

### 3.2 Typical vibration mode of each drug (IR/Raman)

#### Caffeine (MW=194.2)
- C=O stretching: ~1700 cm⁻¹ (~51 THz)
- C=N stretching: ~1600 cm⁻¹ (~48 THz)
- C-N stretch: ~1200-1400 cm⁻¹ (~36-42 THz)
- CH₃ deformation: ~1450 cm⁻¹ (~43 THz)
- THz region (lattice vibration): 0.5~3 THz (NIST database)

#### Diazepam (MW=284.7)
- C=O stretching: ~1690 cm⁻¹ (~50.7 THz)
- C=N stretching (diazepine ring): ~1610 cm⁻¹ (~48.3 THz, Raman)
- Aromatic ring C=C stretching: ~1580-1600 cm⁻¹
- C-Cl stretch: ~750 cm⁻¹ (~22.5 THz)
- Benzodiazepine skeleton: 400-900 cm⁻¹

#### Morphine (MW=285.3)
- O-H stretch: ~3300-3500 cm⁻¹ (~99-105 THz)
- Aromatic ring C-H stretching: ~3050 cm⁻¹
- C=C stretch: ~1600 cm⁻¹
- C-O stretch: ~1050-1250 cm⁻¹
- Low frequency modes: Raman studies identify numerous vibrational bands (Baranska, 2012)

#### Ethanol (MW=46.1)
- O-H stretch: ~3300 cm⁻¹ (~99 THz)
- C-H stretch: ~2900 cm⁻¹ (~87 THz)
- C-O stretch: ~1050 cm⁻¹ (~31.5 THz)
- C-C stretch: ~880 cm⁻¹ (~26.4 THz)

#### Propofol (Propofol, MW=178.3)
- O-H telescopic: ~3600 cm⁻¹
- Aromatic ring C=C stretching: ~1600 cm⁻¹
- C-H deformation: ~1460 cm⁻¹
- Phenolic C-O stretch: ~1200 cm⁻¹
### 3.3 Common points of vibrational characteristics of BBB-passing drugs

IR/Raman vibration bands common to BBB-passing drugs:

| Functional group/vibrational mode | Wavenumber range (cm⁻¹) | Frequency (THz) | Frequency of appearance |
|---|---|---|---|
| C-H expansion and contraction | 2800-3100 | 84-93 | Almost all drugs |
| Aromatic ring C=C expansion and contraction | 1580-1610 | 47-48 | Many drugs |
| C=O stretching | 1650-1700 | 49-51 | Barbiturates, benzodiazepines |
| C-N stretching | 1200-1400 | 36-42 | Nitrogen-containing compounds |
| C-O stretching | 1000-1250 | 30-37 | Many drugs |

**IMPORTANT**: These vibrational modes are dependent on the functional groups of the molecule and are therefore not specific to BBB-crossing drugs. Drugs that do not cross the BBB will exhibit similar frequencies if they have the same functional group.

---

## 4. Hypothesis verification: Relationship between molecular vibration frequency and BBB opening by ultrasound

### 4.1 Organizing hypotheses

> "There is a common feature in the molecular vibration frequency of drugs that pass through the BBB, and BBB opening technology using ultrasound allows drugs to pass through based on principles related to this frequency."

### 4.2 Comparison of frequency scales (most important point)

| Category | Frequency | Hz notation | Notes |
|---|---|---|---|
| **FUS-BBBO Ultrasound** | 200 kHz to 1.5 MHz | 2×10⁵ to 1.5×10⁶ Hz | Macromechanical action |
| **Intramolecular vibration (Mid-IR)** | 10 to 100 THz | 10¹³ to 10¹⁴ Hz | Bond vibrations such as C-H, C=O, etc. |
| **Low frequency molecular vibration (THz)** | 0.1 to 10 THz | 10¹¹ to 10¹³ Hz | Lattice vibration, intermolecular force |

**Frequency Difference**: There is a **approximately 5-9 orders of magnitude (100,000 to 1 billion times) difference** between ultrasound (~10⁵ to 10⁶ Hz) and molecular vibrations (~10¹¹ to 10¹⁴ Hz).

### 4.3 Scientific evaluation of hypotheses

#### Reasons that do not support the hypothesis

1. **Fundamental mismatch in frequency scale**:
   - The frequencies of ultrasound (kHz to MHz) and molecular vibrations (THz to several tens of THz) differ by 5 to 9 orders of magnitude.
   - Frequency matching is necessary for resonance to occur, and molecular resonance is physically impossible with such a difference
   - Example: 51 THz electromagnetic waves are required to resonate the C=O stretching vibration (~51 THz) of caffeine, whereas 500 kHz ultrasound is a completely different physical domain.

2. **FUS-BBBO mechanism is mechanical action**:
- Ultrasound induces expansion and contraction (cavitation) of microbubbles
   - Vibration of the bubble creates physical mechanical stress (shear stress) on the blood vessel wall
   - Tight junction proteins are temporarily reorganized (confirmed in a 2026 Nature paper)
   - This is not **resonance at the molecular level, but mechanical destruction and repair at the cell/tissue level**

3. **Inconsistency with the classical mechanism of BBB crossing**:
   - Passage through the BBB by passive diffusion can be predicted based on molecular weight, fat solubility, and number of hydrogen bonds.
   - Ultrasound is a technology that "passes through drugs that cannot pass through," and its principle is different from "the characteristics of drugs that can originally pass through."
   - After opening the ultrasonic BBB, even antibodies with a molecular weight of tens of thousands of Da can pass through (regardless of vibration characteristics)

4. **Frequency does not explain selectivity across the BBB**:
   - Even if drugs have the same functional group (C=O, C-H, etc.), some will pass through the BBB while others will not.
   - Example: Morphine (crosses the BBB, logP=0.89) and penicillin G (does not cross the BBB, logP=1.83) have similar vibrational bands, but their BBB permeability is very different.

#### Interesting aspects of the hypothesis

However, the following points may merit further study:

1. **Mechanochemical activation of molecules by ultrasound (Sonopharmacology)**:
- Techniques exist where ultrasound waves cause mechanical breaks in polymer chains, releasing drugs.
   - However, this is a covalent bond breakage, not a resonance with molecular vibrations.

2. **Low frequency collective vibration mode**:
   - Proteins and DNA have collective vibrational modes in the GHz band
   - Theoretically there is a non-zero possibility that ultrasound (MHz) and harmonics of these low frequency modes interact, but no experimental evidence exists at this time

3. **Molecular transport by acoustic radiation force**:
   - Ultrasound can enhance transport by exerting a direct radiation force on molecules
   - This effect depends on the acoustic impedance of the molecule, which is a physical quantity separate from the vibration mode.

---

## 5. Conclusion

### Evaluation based on current scientific consensus

| Item | Conclusion |
|---|---|
| Common characteristics of BBB-crossing drugs | Molecular weight < 400 Da, high lipophilicity, few hydrogen bonds (physicochemical properties, not vibrational frequencies) |
| Mechanism of FUS-BBBO | Mechanical tight junction reorganization by microbubble cavitation |
| Relationship between molecular vibrations and ultrasound | **The frequency scales differ by 5 to 9 orders of magnitude, and a direct resonance mechanism does not physically hold** |

### Hypothesis modification suggestions
If we are pursuing vibration-related hypotheses, the following directions are considered more scientifically valid:

1. **Interaction between collective vibration mode (GHz band) of tight junction proteins and ultrasound**: Investigating the possibility that tight junction proteins such as claudin-5 have specific low-frequency vibration modes and that ultrasound affects these

2. **Relationship between vibrational properties of lipid bilayer membranes and membrane permeability of drug molecules**: The lipid membrane of BBB endothelial cells has a specific vibrational mode, and whether drugs that are easy to pass through have dynamic characteristics that match this membrane vibration.

3. **Nanoscale fluid dynamics by acoustic cavitation**: Does the local flow during bubble collapse enable selective transport depending on the size and shape of drug molecules?

---

## References

1. Pardridge WM. Drug transport across the blood-brain barrier. *J Cereb Blood Flow Metab*. 2012;32(11):1959-1972.
2. Banks WA. Characteristics of compounds that cross the blood-brain barrier. *BMC Neurol*. 2009;9(Suppl 1):S3.
3. Pajouhesh H, Lenz GR. Medicinal Chemical Properties of Successful CNS Drugs. *NeuroRx*. 2005;2(4):541-553.
4. Konofagou EE et al. Safe focused ultrasound-mediated blood-brain barrier opening is driven primarily by transient reorganization of tight junctions. *Commun Eng*. 2026.
5. Tung YS et al. The mechanism of interaction between focused ultrasound and microbubbles in blood-brain barrier opening in mice. *J Acoust Soc Am*. 2011;130(5):3059-3067.
6. Chen H, Konofagou EE. The size of blood-brain barrier opening induced by focused ultrasound is dictated by the acoustic pressure. *J Cereb Blood Flow Metab*. 2014;34(7):1197-1204.
7. Baranska M. Morphine studied by vibrational spectroscopy and DFT calculations. *J Raman Spectrosc*. 2012;43(1):102-107.
8. Neville GA et al. Fourier transform Raman and infrared vibrational study of diazepam and related 1,4-benzodiazepines. *J Raman Spectrosc*. 1990;21(1):9-19.
9. Yildiz D, Göstl R, Herrmann A. Sonopharmacology: controlling pharmacotherapy by ultrasound-induced polymer mechanochemistry. *Chem Sci*. 2022.
10. Fernandes TB et al. Analysis of the Applicability and Use of Lipinski's Rule for CNS Drugs. *Lett Drug Des Discov*. 2016;13(10):999-1006.

