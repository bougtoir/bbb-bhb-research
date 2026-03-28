# BBB通過物質に共通する「未確立の要素」— 従来のLipinski則を超えて

## はじめに

BBB通過性を予測する従来の指標（分子量、logP、水素結合数、PSA）は広く確立されているが、これらだけでは説明できない現象が多数存在する。以下に、近年の研究で注目されているが**まだ完全には確立されていない共通要素**を整理する。

---

## 1. 分子の断面積（Cross-Sectional Area, A_D）— 膜内コンフォメーション

### 概要
Seelig（1994, 1998, 2007）による一連の研究で、分子が脂質膜と相互作用する際の**膜結合コンフォメーションにおける断面積（A_D）** がBBB透過の主要決定因子であることが示された。

### 知見
- **A_D < 70 Å²** の分子: BBBを受動拡散で通過可能（P-gpの排出速度を上回る流入）
- **A_D > 80 Å²** の分子: BBBを通過できない（排出が流入を上回る）
- A_D ≈ 50 Å² の分子が最も容易にBBBを通過

### なぜ「未確立」か
- A_Dは界面活性測定や特殊な実験が必要で、一般的な計算記述子ではない
- 分子量やlogPとは独立した情報を含む
- 3D構造に依存するため、2D構造からは容易に予測できない
- **膜の内部横圧（lateral bilayer pressure, π_bi ≈ 34 mN/m）に抗して分子が膜に分配される**という物理モデルに基づいており、単純なlogPモデルより物理的に正確

### 重要性：★★★★★
> **「分子量でも脂溶性でもなく、膜中での分子の"幅"が最も本質的な透過決定因子」** というSeeligの主張は、従来の薬物設計パラダイムを根本的に変える可能性がある。

---

## 2. 衝突断面積（Collision Cross Section, CCS）

### 概要
イオン移動度質量分析法（IM-MS）で測定される**衝突断面積（CCS）** は、2019年にGuntnerらによってBBB透過性の新しい記述子として初めて提案された。

### 知見（Guntner et al., Sci Rep, 2019; Pharmaceutics, 2021）
- 46種の薬理活性分子について、CCSとBBB透過性に**強い相関**を発見
- CCSは質量、構造、体積、分岐度、柔軟性の情報を**単一の測定可能パラメータ**に統合
- BBB+化合物（通過可能）はBBB-化合物（通過不可）より**統計的に有意に小さいCCS**を持つ
- 大規模評価（数千化合物）でも傾向が確認された

### なぜ「未確立」か
- 2019年に初めて提案された非常に新しい記述子
- 計算CCSと実測CCSの信頼性の差が未検証
- 既存のlogP/MW/PSAモデルに対する付加的価値の定量化が不十分
- 専用の質量分析装置が必要

### 重要性：★★★★☆
> CCSは分子の3D形状を反映する**実測可能な物理量**であり、A_Dと概念的に関連する。

---

## 3. カメレオン性（Chameleonicity / Molecular Chameleonic Behavior）

### 概要
「分子カメレオン」とは、環境の極性に応じて**コンフォメーションを動的に変化させ、極性官能基を露出/遮蔽する能力**を持つ分子のこと（Nature Reviews Chemistry, 2023）。

### 知見
- **水性環境**（血液中）: 極性基を露出 → 溶解性確保
- **非極性環境**（脂質膜中）: 分子内水素結合を形成して極性基を遮蔽 → 膜透過性確保
- **ΔPSA（Delta PSA）**: 極性環境と非極性環境でのPSA差として定量化（2026年, Guo et al.）
- シクロスポリンA等の大環状ペプチドが代表例だが、**小分子薬剤でも同様の挙動が報告**
- BBB通過薬剤の多くが「弱い両親媒性」を持ち、環境に応じた適応が可能

### なぜ「未確立」か
- カメレオン性の定量的尺度が統一されていない
- MD（分子動力学）シミュレーションが必要で、高スループットスクリーニングには不向き
- 主にbRo5（beyond Rule of Five）領域の大分子で研究されており、従来の小分子CNS薬への適用は限定的

### 重要性：★★★★☆
> BBB通過薬剤に共通する「環境適応能力」という概念は、静的な物理化学的記述子では捉えられない動的特性である。

---

## 4. 脱溶媒和エネルギー（Desolvation Energy）

### 概要
Fong（2015）は、BBB透過性モデルにおいて**脱溶媒和エネルギー**と**双極子モーメント**が従来見過ごされてきた重要因子であると提唱した。

### 知見
- log PS（BBB透過速度）は以下の4因子に依存:
  1. **脱溶媒和エネルギー**（水和殻を脱ぐエネルギー）
  2. 脂溶性（lipophilicity）
  3. 分子体積
  4. **双極子モーメント**（dipole moment）
- 「脱溶媒和」: 分子が水相から脂質膜に移行するために水和水分子を放出するプロセス
- BBBを通過する分子は**脱溶媒和コストが低い**（水との相互作用が比較的弱い）

### なぜ「未確立」か
- 脱溶媒和エネルギーの正確な計算にはQM（量子化学計算）やMDが必要
- 実験的に直接測定する標準的手法が確立されていない
- logPに部分的に含まれるが、完全には反映されない情報

### 重要性：★★★★☆
> 脱溶媒和は膜透過の**律速段階**の一つであり、logPだけでは説明できないBBB透過性の差を説明できる可能性がある。

---

## 5. 双極子モーメントと分極率（Dipole Moment & Polarizability）

### 概要
分子の電荷分布の非対称性（双極子モーメント）および外部電場への応答性（分極率）がBBB透過に影響する。

### 知見
- Montgomery & Lemkul (2024): 分極可能力場（Drude oscillator）を用いたMDシミュレーションで、膜透過時の**誘起双極子効果**を初めて系統的に定量化
- 分子が脂質二重膜の**誘電勾配**（外側は極性、内側は非極性）を通過する際、分子の双極子が動的に応答
- **分極率が高い分子は膜内での安定化エネルギーが大きく、透過に有利な場合がある**
- ただし効果は分子によって異なり、単純な線形関係ではない

### なぜ「未確立」か
- 分極可能力場によるシミュレーションが最近になって初めて可能になった
- 固定電荷モデル（従来のMD）では捉えられない効果
- BBB特異的な膜組成でのデータが不足

### 重要性：★★★☆☆
> 電子雲の柔軟性が膜透過に寄与する可能性は物理的に合理的だが、実用的な記述子としての有用性は未確定。

---

## 6. LUMO（最低空軌道）エネルギー

### 概要
Wanat & Brzezinska (2023) のクロマトグラフィーデータ分析で、**LUMOエネルギーがBBB透過性予測モデルにおいて有意な記述子**であることが示された。

### 知見
- LUMO（Lowest Unoccupied Molecular Orbital）エネルギーが低い分子は求電子性が高い
- 複数のlog BB回帰モデルにおいて、HBA、HBD、生理的電荷とともに**LUMOエネルギーが有意な因子**として抽出
- 分子の電子受容能力が膜との相互作用パターンに影響する可能性

### なぜ「未確立」か
- QSARモデルでの統計的有意性は示されているが、物理的メカニズムの解釈が不十分
- 他のモデルでは選択されない場合もある（データセット依存性）
- フロンティア軌道エネルギーは計算レベルに強く依存

### 重要性：★★★☆☆

---

## 7. P-gp（P糖蛋白質）排出とのバランス — 「ネットフラックス」概念

### 概要
BBBの内皮細胞にはP-glycoprotein (P-gp/MDR1)等のABCトランスポーターが発現しており、脳に入った薬物を能動的に排出する。BBB通過は単純な「入る/入らない」ではなく、**受動流入と能動排出のバランス（ネットフラックス）** で決まる。

### 知見（Seelig, 2007; Dolghih & Jacobson, 2012）
- CNS薬の大多数はP-gpの**本質的基質**（intrinsic substrate）
- BBBを通過できるのは「受動流入速度 > P-gpによる排出速度」の分子
- **A_D < 70 Å²** かつ低〜中程度の電荷 → 流入 > 排出 → BBB通過
- P-gp排出と受動透過を**組み合わせた予測**は、どちらか単独より優れる

### なぜ「未確立」か
- P-gp基質性の予測自体が困難（多様な基質構造）
- 排出トランスポーターはP-gp以外にもBCRP、MRP等が存在
- ネットフラックスの定量的予測には両方の速度の正確な推定が必要

### 重要性：★★★★★
> **BBB通過＝受動拡散の成功ではなく、流入と排出の競争の結果**という視点は、従来の「通るか通らないか」の二値的な考え方を根本的に変える。

---

## 8. 3D-PSA（三次元極性表面積）と静電ポテンシャルマップ

### 概要
従来のTPSA（Topological PSA）は2D構造に基づく近似値だが、**3D-PSAは分子の実際の3D構造から計算される極性表面積**である。

### 知見（Shityakov et al., 2013）
- 3D-PSAはlog BBとの相関がR² = 0.92（RMSD = 0.29）と非常に高い
- TPSAやSA-2Dよりも予測精度が高い
- 静電ポテンシャルマップから計算される極性表面が、膜との相互作用をより正確に反映

### なぜ「未確立」か
- 3D構造の最適化が必要（コンフォメーション依存）
- 計算コストがTPSAより高い
- 水溶液中vs膜中のコンフォメーション差（カメレオン性）が考慮されていない

### 重要性：★★★★☆

---

## 9. サブストラクチャーの相乗効果（Synergistic Substructural Effects）

### 概要
Kim et al. (2025) は、分子サブストラクチャーの**相乗効果**がBBB透過性に影響することを示した。

### 知見
- 個別の官能基の寄与の単純な足し算ではなく、**組み合わせ（相乗効果）** がBBB+/BBB-を決定
- 正の相乗効果を持つサブストラクチャー群: 芳香環 + 第三級アミン + ハロゲン
- 負の相乗効果: 多数のOH基 + カルボキシル基 + 糖鎖構造
- 説明可能AI（XAI）により相乗効果の可視化が可能に

### なぜ「未確立」か
- サブストラクチャーの定義と分割方法がモデル依存
- 解釈の一般化が困難
- 物理化学的メカニズムとの対応が不明確

### 重要性：★★★☆☆

---

## 10. 膜の横圧（Lateral Bilayer Pressure）との相互作用

### 概要
BBBの内皮細胞膜は他の細胞膜と比較して**コレステロール含有量が高く、脂質パッキングが密**である。このため、膜の内部横圧（lateral pressure profile）が高く、分子の侵入に対する抵抗が大きい。

### 知見
- BBB膜の横圧 π_bi ≈ 34 ± 4 mN/m（Seelig, Fischer & Gottschlich, 1998）
- 膜への分配係数: K_lw = const · K_aw · exp(-A_D · π_bi / kT)
  - A_D（断面積）が大きいほど指数的に分配が減少
  - つまり**膜の横圧に抗して挿入できるかどうか**が透過性を決める
- BBB通過薬剤は、この高い横圧に対抗できる分子形状を持つ

### なぜ「未確立」か
- 膜横圧の直接測定は困難
- 膜組成の違い（血管の種類、疾患状態）による変動が大きい
- 計算的に再現するにはcoarse-grained MDが必要

### 重要性：★★★★☆
> 「BBBが他の生体膜と異なるのは横圧が高いことであり、分子の選択性は横圧と断面積の相互作用で決まる」という視点は、BBB特異性を物理的に説明する。

---

## 総括：未確立要素の優先順位

| 順位 | 要素 | 新規性 | 物理的妥当性 | 実用可能性 | 総合評価 |
|---|---|---|---|---|---|
| 1 | **膜内断面積（A_D）** | 中（1994年提案） | 極めて高い | 低（測定困難） | ★★★★★ |
| 2 | **ネットフラックス（流入vs排出）** | 中 | 極めて高い | 中 | ★★★★★ |
| 3 | **衝突断面積（CCS）** | 高（2019年） | 高い | 中（IM-MS必要） | ★★★★☆ |
| 4 | **カメレオン性（ΔPSA）** | 高 | 高い | 低（MD必要） | ★★★★☆ |
| 5 | **脱溶媒和エネルギー** | 中 | 高い | 低 | ★★★★☆ |
| 6 | **3D-PSA** | 中 | 高い | 中 | ★★★★☆ |
| 7 | **膜横圧との相互作用** | 中 | 極めて高い | 低 | ★★★★☆ |
| 8 | **双極子モーメント/分極率** | 中 | 中〜高 | 中 | ★★★☆☆ |
| 9 | **LUMOエネルギー** | 中 | 中 | 高い | ★★★☆☆ |
| 10 | **サブストラクチャー相乗効果** | 高 | 低〜中 | 中 | ★★★☆☆ |

---

## 結論：BBB通過物質に共通する「本質的な特徴」の候補

従来の「小さくて脂溶性が高い」という理解を超えた、より本質的な共通要素は：

1. **「膜中での分子の幅が狭い」こと（A_D < 70 Å²）** — 分子量やlogPよりも直接的にBBB透過性を決定する可能性がある。BBB通過薬剤は、脂質膜に挿入される際のコンフォメーションが「細長い」形状をとる傾向がある。

2. **「環境に応じて姿を変えられる」こと（カメレオン性）** — 水中では親水性表面を見せ、膜中では疎水性表面を見せる動的能力。BBB通過薬剤は分子内水素結合による自己遮蔽能力を持つ傾向がある。

3. **「水を手放しやすい」こと（低い脱溶媒和コスト）** — 膜への移行の律速段階は水和殻の放出であり、BBB通過薬剤は水との結合が比較的弱い。

4. **「排出ポンプに勝てる」こと** — P-gpの基質であっても、受動流入速度が排出速度を上回れば通過可能。断面積が小さく電荷が低い分子がこの競争に勝つ。

---

## 参考文献

1. Seelig A. A method to determine the ability of drugs to diffuse through the blood-brain barrier. *PNAS*. 1994;91(1):68-72.
2. Fischer H, Gottschlich R, Seelig A. Blood-brain barrier permeation: molecular parameters governing passive diffusion. *J Membr Biol*. 1998;165:201-211.
3. Seelig A. The role of size and charge for blood-brain barrier permeation of drugs and fatty acids. *J Mol Neurosci*. 2007;33:32-41.
4. Guntner AS et al. Collision cross sections obtained with ion mobility mass spectrometry as new descriptor to predict blood-brain barrier permeation by drugs. *Sci Rep*. 2019;9:19182.
5. Guntner AS et al. Large-scale evaluation of collision cross sections to investigate blood-brain barrier permeation of drugs. *Pharmaceutics*. 2021;13:2141.
6. Ermondi G et al. Molecular chameleons in drug discovery. *Nat Rev Chem*. 2023.
7. Fong CW. Permeability of the blood-brain barrier: molecular mechanism of transport of drugs. *J Membr Biol*. 2015;248:651-669.
8. Montgomery JM, Lemkul JA. Quantifying induced dipole effects in small molecule permeation in a model phospholipid bilayer. *J Phys Chem B*. 2024;128:7385-7400.
9. Wanat K, Brzezinska E. Chromatographic data in statistical analysis of BBB permeability indices. *Membranes*. 2023;13:623.
10. Dolghih E, Jacobson MP. Predicting efflux ratios and blood-brain barrier penetration from chemical structure. *ACS Chem Neurosci*. 2012;4:361-367.
11. Shityakov S et al. Analysing molecular polar surface descriptors to predict blood-brain barrier permeation. *IJCBDD*. 2013;6(1/2):146-156.
12. Kim HW et al. Explaining blood-brain barrier permeability by synergistic effect on molecular substructures. 2025.
13. Guo Z et al. Delta PSA: A new metric for conformational dynamics underlying macrocyclic peptide permeability. *bioRxiv*. 2026.
14. Spielvogel CP et al. Enhancing blood-brain barrier penetration prediction by machine learning. *J Chem Inf Model*. 2025;65:2773-2784.
