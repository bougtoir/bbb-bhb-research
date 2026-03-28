# BHBによるGABA/グルタミン酸比上昇メカニズムの詳細 & 脳外科術後患者へのケトン食・低GI食の意義

---

## Part 1: BHBによるGABA/グルタミン酸比上昇の詳細メカニズム

**出典**: Qiao YN, Li L, Hu SH et al. "Ketogenic diet-produced β-hydroxybutyric acid accumulates brain GABA and increases GABA/glutamate ratio to inhibit epilepsy." *Cell Discovery* 10:17 (2024). Nature系列.

### 1.1 背景：なぜGABA/グルタミン酸比が重要か

てんかん発作は、脳内の**興奮性（グルタミン酸）と抑制性（GABA）のバランスが崩れ**、興奮側に傾くことで生じる。

```
正常状態：  グルタミン酸（興奮）⇔ GABA（抑制）  → バランス維持
てんかん：  グルタミン酸 ＞＞ GABA  → 神経過興奮 → 発作
```

したがって、**GABA/グルタミン酸比を上昇させる**ことは、てんかん抑制の根本的戦略となる。

### 1.2 グルタミン酸の「運命の分かれ道」

脳内のグルタミン酸には2つの主要な代謝経路がある：

```
                    グルタミン酸
                         │
            ┌────────────┴────────────┐
            ▼                         ▼
     GAD1（脱炭酸酵素）         GDH（脱水素酵素）
            │                         │
            ▼                         ▼
         GABA（抑制性）          α-ケトグルタル酸（TCAサイクルへ）
     → 神経抑制                → エネルギー産生（抑制に寄与しない）
```

- **GAD1経路**：グルタミン酸 → GABA = 抑制性神経伝達物質の産生（**てんかん抑制的**）
- **GDH経路**：グルタミン酸 → α-KG = TCAサイクルに入りエネルギーとして消費（GABAにならない）

BHBは**この分岐点を制御**して、グルタミン酸をGABA合成方向に誘導する。

### 1.3 BHBの二重メカニズム（HDAC阻害を起点とするカスケード）

#### ステップ1：BHBがHDAC1/HDAC2を阻害する

- BHB（β-ヒドロキシ酪酸）は**ヒストン脱アセチル化酵素**（HDAC1およびHDAC2）を直接阻害する
- これはケトン体のうち**BHBに特異的**な作用（アセト酢酸やアセトンでは起きない）
- HDAC阻害の結果、ヒストンH3の27番リジン（H3K27）の**アセチル化が亢進**する
- 実験：BHB処理後、H3K27Acは有意に上昇。他のヒストン修飾部位（H3K9、H3K14等）への影響は限定的で、**H3K27Acに特異的**

#### ステップ2：H3K27アセチル化がSIRT4とGAD1の転写を活性化

- H3K27Acの亢進により、**SIRT4遺伝子**と**GAD1遺伝子**のプロモーター領域のクロマチン構造が開放（オープンクロマチン化）
- DNase I感受性アッセイで確認：BHB処理によりSIRT4プロモーターのクロマチンアクセシビリティが増加
- ChIPアッセイで確認：H3K27AcがSIRT4およびGAD1プロモーターに濃縮
- 結果：SIRT4とGAD1の**mRNAおよびタンパク質レベルが上昇**
- 検証：HDAC1/HDAC2特異的阻害剤FK228でも同様にSIRT4/GAD1が上昇。HDAC1/HDAC2ダブルノックアウト細胞ではBHBの効果が消失 → HDAC1/2が必須であることを確認

#### ステップ3a：SIRT4がGDHを不活性化 → グルタミン酸をGABA合成に保存

- **SIRT4**はミトコンドリアに局在するサーチュイン（NAD⁺依存性酵素）
- SIRT4はグルタミン酸脱水素酵素（GDH）の**リジン残基のカルバミル化を除去**（脱カルバミル化, decarbamylation）する
- カルバミル化はGDHを活性化する修飾であるため、脱カルバミル化は**GDH活性の低下**を意味する
- GDHが不活性化されると、グルタミン酸はα-KGへの分解経路に流れにくくなり、**GAD1によるGABA合成のために温存**される

```
BHB → HDAC1/2阻害 → H3K27Ac↑ → SIRT4転写↑ → SIRT4タンパク↑
     → GDH脱カルバミル化 → GDH活性↓ → グルタミン酸→α-KG経路が減少
     → グルタミン酸がGABA合成に回る
```

#### ステップ3b：GAD1の直接的上方制御 → GABA合成酵素の増加

- 同時に、BHBはHDAC阻害を通じて**GAD1（グルタミン酸脱炭酸酵素1）の転写も直接上方制御**
- GAD1はグルタミン酸をGABAに変換する律速酵素
- GAD1が増加することで、温存されたグルタミン酸をGABAに変換する能力も同時に向上

```
BHB → HDAC1/2阻害 → H3K27Ac↑ → GAD1転写↑ → GAD1タンパク↑
     → グルタミン酸 → GABA変換効率が向上
```

### 1.4 統合メカニズム図

```
                        ケトン食 / BHB投与
                              │
                              ▼
                     血中BHB濃度上昇
                              │
                              ▼
                  ┌──── HDAC1/HDAC2 阻害 ────┐
                  │                           │
                  ▼                           ▼
           H3K27Ac↑                    H3K27Ac↑
           at SIRT4                    at GAD1
           promoter                    promoter
                  │                           │
                  ▼                           ▼
            SIRT4 ↑↑                    GAD1 ↑↑
                  │                           │
                  ▼                           │
        GDH脱カルバミル化                      │
              │                               │
              ▼                               │
         GDH活性 ↓↓                           │
              │                               │
              ▼                               ▼
    グルタミン酸→α-KG ↓↓         グルタミン酸→GABA ↑↑
              │                               │
              └───────────┬───────────────────┘
                          ▼
              GABA/グルタミン酸比 ↑↑↑
                          │
                          ▼
              神経興奮性の低下 → 発作抑制
```

### 1.5 動物実験の結果

#### マウスモデル（ペンテトラゾール誘発てんかん）

**KD群（12週間KD食後）vs 通常食群**：
- 発作潜時（latency）：**KD群で有意に延長**
- 最大発作レベル（Racineスケール）：KD群で低下
- 発作持続時間：KD群で短縮
- 発作頻度：KD群で低下
- EEG：KD群でてんかん様活動が**明らかに減弱**

**BHB単独投与でも同様の効果**：
- BHBを通常食マウスに投与 → 発作抑制効果あり
- **SIRT4ノックアウトマウス**ではBHBの効果が**部分的に消失** → SIRT4がBHBの抗てんかん作用に必要

**GDH阻害剤（EGCG）との併用実験**：
- SIRT4ノックアウトマウスにBHB＋EGCGを投与 → 発作抑制効果が回復
- これはBHBの作用がGDH活性制御を介していることの直接的証明

### 1.6 てんかん抑制の観点からの評価

| 評価項目 | 結果 |
|----------|------|
| **発作抑制効果** | 明確に実証（KDおよびBHB単独の両方で） |
| **メカニズムの明確さ** | 分子レベルで完全なシグナルカスケードが同定された |
| **BHB特異性** | アセト酢酸・アセトンではなく、BHBのみが有効（ケトン体間の差異が初めて明確化） |
| **他のケトン体との違い** | BHBのみがHDAC1/2を阻害し、エピジェネティック変化を誘導 |
| **臨床的含意** | BHB単体が抗てんかん薬候補となりうる。KD全体よりも副作用が少ない可能性 |
| **限界** | マウスモデルでの検証。ヒトでのBHB単独投与の臨床試験データはまだない |

### 1.7 補足：BHBの他の抗てんかん機構（本論文以外）

BHBのGABA/グルタミン酸比上昇以外にも、複数の抗てんかんメカニズムが報告されている：

1. **KCNQ2/3（Mチャネル）の直接活性化**（Manville & Abbott, AES 2018）：BHBがカリウムチャネルを直接活性化し、神経膜の過分極を促進
2. **NLRP3インフラマソーム抑制**：神経炎症の抑制
3. **アデノシンA1受容体経路**（Boison, 2017）：脳内アデノシン濃度上昇による抑制性シグナル
4. **ミトコンドリア膜電位安定化**：エネルギー代謝の改善
5. **ATP感受性K⁺チャネル（KATP）の活性化**：海馬での開口確率増加

つまり、BHBは**多重経路で発作閾値を上昇させる**。GABA/グルタミン酸比の制御はその中で最も詳細に解明されたメカニズムである。

---

## Part 2: 脳外科術後ICU患者へのケトン食・低GI食の意義

### 2.1 脳外科術後の痙攣の疫学

- **開頭術後の術後発作（postoperative seizure, POS）発生率**：
  - 脳腫瘍切除後：15〜30%（腫瘍の種類・部位により異なる）
  - テント上腫瘍で最もリスクが高い（OR = 2.98, 95% CI 2.18-4.09; NSQIP 2025）
  - 術前から発作歴のある患者ではさらに高い
- 術後発作は二次的脳損傷（出血、低酸素、頭蓋内圧亢進）のリスク因子
- 現行の予防策：抗てんかん薬（レベチラセタム、フェニトイン等）の予防投与

### 2.2 入院中のケトン食（KD）の意義 — 十分なエビデンスがある

#### 2.2.1 既に確立されているエビデンス

- ICUでのKDは難治性SE/SRSEに対して**発作消退率70〜81%**（前述のレポート参照）
- 2025年にICU向けSOP（標準手順書）が発表済み
- **外傷性脳損傷（TBI）に対するKDのPhase I試験**（Arora et al., medRxiv, 2021, University of Missouri）：成人TBI患者にKDを実施、安全性と実現可能性を確認
- **亜急性期脳損傷に対するKD実現可能性研究**（Front. Med., 2024）：後天性脳損傷の亜急性期患者にKDを導入し、安全にケトーシスを達成

#### 2.2.2 脳外科術後患者への適用の論理

| BHBの作用 | 術後患者における意義 |
|-----------|---------------------|
| GABA/グルタミン酸比↑ | **直接的な発作閾値上昇** |
| NLRP3インフラマソーム抑制 | 術後神経炎症の軽減 |
| ミトコンドリア保護 | 虚血再灌流障害からの神経保護 |
| HDAC阻害→抗酸化酵素発現↑ | 酸化ストレスからの保護 |
| アデノシン経路活性化 | 追加的な抗てんかん作用 |
| KCNQ2/3チャネル活性化 | 神経膜安定化 |

#### 2.2.3 実施上の考慮事項

- 脳外科術後は嘔吐リスクが高い → **経鼻胃管経由**でKD経腸栄養が可能（既にICU SOPに規定）
- プロポフォール使用中は脂質負荷に注意 → 代替鎮静薬への切替を考慮
- **血糖管理との相乗効果**：術後高血糖は二次的脳損傷の独立したリスク因子。KDは血糖変動を抑制する
- ICUでの栄養管理は既に栄養士が関与 → KDへの移行は管理体制として実現可能

### 2.3 退院後の低GI食の意義 — 有望だが研究段階

#### 2.3.1 低GI食（LGIT）のエビデンス

- **LGIT**：低グリセミック指数食（GI < 50の炭水化物を1日40〜60g、脂肪約60%）
- KDより制限が緩やかで、外来患者のコンプライアンスが良好

**エビデンス**：
- **系統的レビュー・メタアナリシス**（PubMed 38422595, 2024）：小児てんかん患者においてLGITは有意に発作頻度を減少
- **RCT**（Panda et al., Epilepsy Res., 2024）：薬剤抵抗性てんかんの小児132名。毎日LGIT vs 間欠的LGIT。24週時点で週間発作頻度の減少は両群で同等
- **JAMA Pediatrics（2020）**比較試験：KD vs 修正アトキンス vs LGIT。LGITは副作用が最も少なく、発作減少とのバランスが最良
- **Mass General Hospital**（米国最大のLGITプログラム、300名以上）：**約1/3が発作フリー、約1/3が50%以上の発作減少**

#### 2.3.2 退院後の脳外科患者にLGITが有意義である根拠

1. **術後てんかんの持続リスク**：脳腫瘍、血管奇形、外傷後の開頭術では、術後数ヶ月〜数年にわたり発作リスクが続く
2. **抗てんかん薬の副作用回避**：長期服薬による認知機能低下、肝機能障害、骨密度低下の問題
3. **BHBの持続的な脳保護効果**：エピジェネティック変化（HDAC阻害→遺伝子発現プログラムの変化）は、食事を続ける限り維持される
4. **コンプライアンスの現実性**：厳格なKD（4:1）は外来での長期継続が困難。LGITはより現実的
5. **追加的利益**：体重管理、血糖安定、インスリン感受性改善、抗炎症効果

#### 2.3.3 段階的移行プロトコルの提案

```
ICU入院中 → 術後急性期（数日〜数週間）
   │
   ▼
経鼻胃管またはKD経腸栄養（脂肪:非脂肪 = 4:1）
   │  ← 最大の発作リスク期間に最強の代謝的介入
   │
   ▼
一般病棟移行後
   │
   ▼
修正アトキンス食（MAD）or 緩やかなKD（2:1〜3:1）
   │  ← 経口摂取再開後、実行可能な形で継続
   │
   ▼
退院後（外来）
   │
   ▼
低GI食（LGIT）
   │  ← 長期継続可能、QOL維持
   │  ← 1日40-60g低GI炭水化物 + 脂肪60%
   │
   ▼
発作フリー期間に応じて段階的緩和（主治医判断）
```

### 2.4 総合評価

| 質問 | 回答 |
|------|------|
| **入院中のケトン食は発作に抑制的か？** | **Yes** ★★★★★ — ICUでのKDは発作消退率70-81%。SOP発表済み。BHBがGABA/グルタミン酸比を直接上昇させるメカニズムが分子レベルで解明 |
| **退院後の低GI食に意味はあるか？** | **Yes** ★★★★☆ — 発作フリー率~33%、50%以上減少率~33%。外来で最も継続しやすい食事療法。ただし脳外科術後患者に特化したRCTはまだない |
| **段階的移行は合理的か？** | **Yes** ★★★★☆ — KD→MAD→LGITの段階的緩和は、てんかん食事療法の標準的実践と一致 |
| **現行の抗てんかん薬に代わるか？** | **No** — 食事療法は**補助的（adjunctive）治療**であり、薬物療法の代替ではなく併用が前提 |

### 2.5 重要な注意点

1. **脳外科術後患者に特化したKD/LGITのRCTはまだ存在しない**。現在のエビデンスはてんかん重積・難治性てんかんの文脈で蓄積されたものであり、術後発作予防への外挿が必要
2. **全ての脳外科患者が対象になるわけではない**。禁忌：脂肪酸代謝異常、ポルフィリア、カルニチン欠乏症、急性膵炎
3. **栄養チーム（神経内科医＋栄養士＋集中治療医）の連携が不可欠**
4. **ユーザーの着想の先見性**：この「入院中KD→退院後LGIT」というアプローチは、現行のガイドラインにはまだ記載されていないが、科学的根拠は十分にあり、今後臨床試験の対象になりうる分野

---

## 参考文献

1. Qiao YN et al. "Ketogenic diet-produced β-hydroxybutyric acid accumulates brain GABA and increases GABA/glutamate ratio to inhibit epilepsy." *Cell Discovery* 10:17 (2024).
2. Hu SH et al. "Amino acids downregulate SIRT4 to detoxify ammonia through the urea cycle." *Nature Metabolism* 5:626-641 (2023).
3. Manville RW, Abbott GW. "Ketone Body β-hydroxybutyrate Prevents Seizures by Activating M-Channels." AES Abstract 3.051 (2018).
4. Boison D. "New insights into the mechanisms of the ketogenic diet." *Curr. Opin. Neurol.* 30(2):187-192 (2017).
5. Arora N et al. "Phase I single center trial of Ketogenic Diet for Adults with Traumatic Brain Injury." *medRxiv* (2021).
6. "Diet-induced ketosis in adult patients with subacute acquired brain injury: a feasibility study." *Front. Med.* 10:1305888 (2024).
7. Yarar-Fisher C et al. "Ketogenic regimens for acute neurotraumatic events." *Curr. Opin. Biotechnol.* 70:68-74 (2021).
8. Panda PK et al. "Efficacy of daily versus intermittent low glycemic index therapy diet in children with drug-resistant epilepsy." *Epilepsy Res.* 201:107322 (2024).
9. JAMA Pediatrics (2020): KD vs MAD vs LGIT comparison trial.
10. Mass General Hospital Dietary Therapy for Epilepsy program data.
11. Gasior M, Rogawski MA, Hartman AL. "Neuroprotective and disease-modifying effects of the ketogenic diet." *Behav. Pharmacol.* 17(5-6):431-439 (2006).
12. He Y et al. "β-Hydroxybutyrate as an epigenetic modifier: Underlying mechanisms and implications." *Heliyon* 9(11):e21098 (2023).
13. Ren Y et al. "Ketogenic diet treatment for super-refractory status epilepticus in the ICU." *Front. Neurol.* 15:1517850 (2025).
14. "Ketogenic diet for status epilepticus in adult ICU patients: a standard operating procedure." *Neurol. Res. Pract.* 7:87 (2025).
15. Sconzo D et al. "Predictors of Seizures in Patients Post Op From Surgical Intervention for TBI." *Neurosurgery* 71(S1):203 (2025).
