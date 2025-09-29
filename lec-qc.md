---
marp: true
html: true
title: slides
paginate: true
math: mathjax
size: 16:9
style: |
  @import "themes/mytheme01.css";
---
<!--
headingDivider: 1
-->
<!--
_class: title
-->
# 量子計算機
<br>
光成滋生

# 概要
## 古典計算機
- 現在（古典）計算機はビット (0 or 1) を基本単位として計算
- 論理ゲート: AND, OR, NOTなどのビット演算の組合せ
## 量子計算機
- 量子力学で記述される現象を利用した新しい計算機
- 量子計算機の発展は暗号技術に対して重大な影響がある
  - 対策: 耐量子計算機暗号, 量子鍵配送（量子暗号）
## 粒子と波
- 粒子は1個, 2個と数えられ, 同じ場所に複数個存在できない
- 波は数えられない広がりを持った状態
- 複数の波が重なり合って干渉する

# 量子計算機 QC (Quantum Computer)
<!-- _class: image-right -->
![w:500px](images/lec-qc1.drawio.svg)
## 量子の性質を利用した計算機
- 量子: 粒子と波の両方の性質を持ったもの
- 0の状態を$|0\rangle$, 1の状態を$|1\rangle$と表す
- 量子ビット (qubit) : QCの基本単位
  - qubit : $|\psi\rangle:=a|0\rangle + b|1\rangle$
    - $a, b \in \mathbb{C}$, $|a|^2+|b|^2=1$
    - $(|0\rangle, |1\rangle)$ は複素2次元ベクトル空間の基底
## 観測
- $|\psi\rangle$ を基底 $(|0\rangle, |1\rangle)$ に従って「観測」すると
$|a|^2$ の確率で $|0\rangle$, $|b|^2$ の確率で $|1\rangle$ が得られる（詳しい話はここではしない）
- $θ$ を実数として $|\psi'\rangle:=e^{iθ} |\psi\rangle$ を観測しても同じ確率（$|e^{iθ}|=1$ なので）
- $|\psi\rangle$ と $|\psi'\rangle$ は物理的に区別がつかない: $e^{iθ}$ を位相因子, 位相変換に対して不変という

# 量子ゲート : qubitの状態を変換する演算
## ユニタリ行列
- $|0\rangle$ を $\begin{pmatrix}1 \\ 0\end{pmatrix}$, $|1\rangle$ を $\begin{pmatrix}0 \\ 1\end{pmatrix}$ と表すと $|\psi\rangle$ を $a|0\rangle + b|1\rangle=\begin{pmatrix}a \\ b\end{pmatrix}$ と表現できる
- 2行2列の複素行列 $U$ で $U^\dagger U = I$ を満たすものをユニタリ行列という
  - $U^\dagger$ は $U$ の転置＋複素共役を表す
## 量子ゲート
- 複素2次元ベクトル $\begin{pmatrix}a \\ b\end{pmatrix}$ にユニタリ行列 $U$ を掛ける操作を量子ゲートという
- $U$ がユニタリ行列なら $U^{-1}=U^\dagger$ なので $U$ は可逆
- 量子ゲートは可逆な変換しかできない
  - 例えば古典の AND ゲートは不可逆なので量子ゲートでは実現できない
  - $(x,y,z) \mapsto (x, y, z \oplus (x \land y))$ のように入力を保存する形で実現する

# 量子ゲートの例
## 代表的な量子ゲート
- X (NOT) ゲート: $X:=\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}$, $X|0\rangle = |1\rangle$, $X|1\rangle = |0\rangle$: 基底の反転
- アダマールゲート: $H:=\frac{1}{\sqrt{2}}\begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}$, $H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$, $H|1\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$
- $|+\rangle := H|0\rangle$, $|-\rangle := H|1\rangle$ と表記することが多い（$(|+\rangle, |-\rangle)$ も別の基底）
  - このとき $|0\rangle=\frac{1}{\sqrt{2}}(|+\rangle + |-\rangle)$, $|1\rangle=\frac{1}{\sqrt{2}}(|+\rangle - |-\rangle)$
  - 基底$(|+\rangle, |-\rangle)$に従って $|1\rangle$ を観測すると $|-\rangle$ が得られる確率は $1/2$
- 異なる基底での観測
![w:900px](images/lec-qc3.drawio.svg)

# 複数個のqubit
## テンソル積
- 2個の2次元ベクトルの基底を組み合わせて4次元ベクトル空間の基底を作る（合成系という）
  - $(a,b)\otimes (c,d):=(ac, ad, bc, bd)$ （表記の都合で横ベクトルで表す）
- 独立に準備された2個の1 qubit $|\psi_1\rangle$ と $|\psi_2\rangle$ がある状態を $|\psi_1\rangle \otimes |\psi_2\rangle$ と表す
- 複素4次元ベクトル空間 $\cal H$ の基底
  - $|00\rangle:=|0\rangle \otimes |0\rangle = (1,0) \otimes (1,0)=(1,0,0,0)$
  - $|01\rangle:=|0\rangle \otimes |1\rangle = (1,0) \otimes (0,1)=(0,1,0,0)$
  - $|10\rangle:=|1\rangle \otimes |0\rangle = (0,1) \otimes (1,0)=(0,0,1,0)$
  - $|11\rangle:=|1\rangle \otimes |1\rangle = (0,1) \otimes (0,1)=(0,0,0,1)$
- 一般に $\cal H$ の元は $c_{00}|00\rangle + c_{01}|01\rangle + c_{10}|10\rangle + c_{11}|11\rangle$ ($c_{ij} \in \mathbb{C}$, $\sum |c_{ij}|^2=1$) の形
  - この基底で観測したとき $|ij\rangle$ が得られる確率は $|c_{ij}|^2$
- $n$個のqubitの状態は $2^n$ 次元複素ベクトルとなる

# 量子もつれ (Entanglement)
## 合成系の中でテンソル積で表現できない状態
- テンソル積で表現できる例
  - $\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \otimes |0\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle)$
  - $\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \otimes \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)=(|00\rangle + |01\rangle + |10\rangle + |11\rangle)/2$
- テンソル積で表現できない例
  - $\psi:=\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$
    - $\psi = \psi_1 \otimes \psi_2$ と表現できない（なぜ?）
  - このとき $\psi$ は量子もつれの状態にあるという
## 独立性
- 1個目のqubitを観測して $|0\rangle$ が得られたら2個目も $|0\rangle$, $|1\rangle$ が得られたら2個目も $|1\rangle$
- 1個目のqubitの状態が決まると2個目の状態も決まる（2個のqubitが独立ではない）

# CNOT (Controlled NOT) ゲート
## 2個のqubitに対する量子ゲート
- $CNOT(a|00\rangle + b|01\rangle + c|10\rangle + d|11\rangle):=a|00\rangle + b|01\rangle + d|10\rangle + c|11\rangle$
  - 後ろ2個の基底の係数が入れ代わる
  ![w:400px](images/lec-cnot1.drawio.svg) ![w:600px](images/lec-cnot2.drawio.svg)
  - 状態 $|x y\rangle$ ($x, y \in \Set{0,1}$) に対して $x=0$ のとき $y$ はそのまま, $x=1$ のとき $y$ は反転
  - $(x, y) \mapsto (x, x \oplus y)$ と表せる
- $x= \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$, $y=|0\rangle$ とすると $x \otimes y = \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle)$
  - $CNOT(x \otimes y)=\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$ となり量子もつれの状態になる
- 1 qubitの量子ゲートとCNOTゲートを組み合わせると任意のゲートを構成できる（定理）

# 量子計算機 QC における計算
<!-- _class: image-right-center -->
![w:470px](images/lec-qc-algo.png)
## $n$ qubitの状態
- $n$ bitのデータは $2^n$ 通りのパターンのどれか一つを表す
- $n$ qubitの状態は $2^n$ 通りのパターンが重なり合った状態を表す
  - $|\psi\rangle = \sum_{i=0}^{2^n-1} c_i |i\rangle$ ($c_i \in \mathbb{C}$, $\sum |c_i|^2=1$)
  - $|i\rangle$ は $i$ を2進数展開($i=\sum_k i_k 2^k$)して $|i_0 i_1 \cdots i_{n-1}\rangle$ の略記
## QCの処理
- $|\psi\rangle$ に量子ゲート（ユニタリ行列）を繰り返し作用させる
  - 原理的に1回で $2^n$ 個のパターンを処理できる
- ただし最終的には観測しないと結果を得られない
  - そのとき $|c_i|^2$ の確率で $|i\rangle$ に確定し, これが計算結果となる
- もし $|c_0| = \dots = |c_{2^n-1}|$ ならどの $|i\rangle$ が得られるか完全にランダム
- 望ましい答えが観測されるように $|c_i|$ を大きくするのがQCアルゴリズム

# 一般の関数に対する量子ゲート
## 補助ビット (ancilla) の導入
- 関数 $f : \Set{0,1}^n \to \Set{0,1}$ に対して
$U_f : |x\rangle \otimes |y\rangle \mapsto |x\rangle \otimes |y \oplus f(x)\rangle$ と定義する
  - $x$: $n$ qubit, $y$: 1 qubit （$y$ が補助ビット）
- このとき $U_f$ はユニタリ行列になる
  - $U_f(U_f(|x\rangle \otimes |y\rangle)) = |x\rangle \otimes |y \oplus f(x) \oplus f(x)\rangle = |x\rangle \otimes |y\rangle$
  - つまり $U_f^{-1} = U_f$

# Groverのアルゴリズム
## $N$ 個のデータから特定の条件を満たすものを一つ探す
- 関数 $f(x) = 1$ if $x=a$, それ以外は0 において $f(x)=1$ となる $x=a$ を探す
- 古典計算機なら平均 $N/2$ 回の試行が必要
- Groverのアルゴリズムは $O(\sqrt{N})$ 回の量子クエリで可能
  - $O(\sqrt{N})$ 回のクエリで十分高い確率で $f(x)=1$ なる $x$ が見つかるということ
![w:700px](images/lec-grover.png)

# Shorのアルゴリズム
## $n=pq$ ($p$, $q$ は素数) を素因数分解するアルゴリズム
- $g \in [1, n-1]$ をとり $g^r \equiv 1 \pmod{n}$ となる最小の正整数 $r$ を求める（$g$ の位数という）
- $r$ が偶数ならば $(g^{r/2} - 1)(g^{r/2} + 1) \equiv 0 \pmod{n}$
  - このとき有意な確率で $\gcd(g^{r/2}-1,n)$ は $n$ の真の約数となることが知られている
  - $\gcd$ は古典計算機でも高速に求められるので $g$ の位数を高速に求められればよい
- 全体で $O((\log n)^3)$ で素因数分解できることが知られている
## 量子位相推定 QPE (Quantum Phase Estimation)
- $U|\psi\rangle = e^{2\pi i θ} |\psi \rangle$ となる $U$, $\psi$ が与えられたとき $θ$ を精度よく求める
- QPEは量子フーリエ変換 QFT (Quantum Fourier Transform) を利用して効率よく求められる
- QFT : フーリエ変換の量子版
  - $U|x\rangle=1/\sqrt{2^n} \sum_y \exp(2\pi ixy/2^n)|y\rangle$
  - うまい方法を使うと $O(n^2)$ 個の量子ゲート, $O(n^2)$ ステップで実現可能

# 量子計算機 QCとECDLP
## ECDLP
- 楕円曲線 $E/\mathbb{F}_p$ 上の点 $P$, $Q$ が与えられたとき $Q=r P$ となる $r$ を求める問題
- QPEを利用して $O((\log p)^3)$ で解けることが知られている
- ビット数が少ない分, 素因数分解よりも効率よく求められる
  - 古典計算機と逆の状況

# 量子計算機の課題
## コヒーレンス時間
- 量子状態を保っていられる時間
- コヒーレンス時間が短いと長時間動作させられない
## 誤り訂正
- 量子状態は外部環境の影響を受けやすく誤りが発生しやすい
- 誤り訂正の技術を使って複数の物理qubitで1個の論理qubitを表す
- 実際に計算できるためには誤り耐性量子計算（FTQC : Fault-Tolerant QC）が必要
- 実用的なものは100万 qubit程度必要と言われている
## メモリ
- 現在のQCは量子メモリを持たない
- 必要な情報は全てqubitで表現する

# 量子計算機の方式
## 様々な方式が提案・実現されている

方式|コヒーレンス時間|速度|誤り率|温度|5~6年の目標
---|---|---|---|---|---
超電導|10~200μs|~100ns|0.1%|~10mK|$10^5$
イオントラップ|分|~100μs|0.01%|室温|$10^3$
中性原子|~100ms|10μs|0.1%|~1mK|$10^5$
光|無制限|ps|0.1%|室温|$100 \sim 200$

- 数値はぶれが大きく・方式が異なるものの比較も難しいのであくまで参考値
- [1qubitで1/670万のエラー率](https://qiqb.osaka-u.ac.jp/newstopics/pr20250623)の報告
- qubitを増やすだけでなくエラー率の低減・運用コストなども課題

# 量子計算機の実装例
## 超伝導方式
- Google: 2019年 53 qubit, 2024年 105 qubit
- [IBMのロードマップ](https://www.ibm.com/quantum/technology#roadmap): 2021年 127 qubit, 2022年 433 qubit, 2023年 1121 qubit Condor
- 大阪大学: 2023年 [64 quibit](https://resou.osaka-u.ac.jp/ja/research/2023/20231220_1), 富士通と理研: 2025年 [256 qubit](https://pr.fujitsu.com/jp/news/2025/04/22.html)
## イオントラップ方式
- 2023/6 : [IonQが29 quibit](https://ionq.com/posts/ionq-achieves-new-performance-milestone-of-29-algorithmic-qubits-aq-on-ionq), 2025: Quantinuum 56 qubit
## 中性原子方式
- 2023/10 : Atom Computing [1180 quibit](https://atom-computing.com/quantum-startup-atom-computing-first-to-exceed-1000-qubits/)
## その他
- 電子, 光, マイクロ波 etc.

# 素因数分解の評価
## 理論的には
- Beauregard (2003)の見積もりで $n$ bitの数の素因数分解に $2n+3$ bit必要
## 実際に必要なqubitの見積もり
- [Gidney and Ekerå (2019)](https://arxiv.org/abs/1905.09749) : 2048 bit RSAを解くにはエラー率0.1% 2000万 qubit, 8時間
- [Gidney (2025)](https://arxiv.org/abs/2505.15917)（未査読）: 2048 bit RSAを解くにはエラー率0.1% 100万 qubit, 1週間
## 実際に解読できたパターン
- 2001 IBM : 15 = 3x5
- 2012 [Josephson phase qubi](https://arxiv.org/abs/1202.5707) : 21 = 3x7
- 2019 IBM : 35を素因数分解しようとしたが失敗
- (DLP) 2020 [NICT](https://www.nict.go.jp/press/2020/12/09-1.html) : $2^x\equiv 1 \pmod{2}$ は解けたが $4^x \equiv 2 \pmod{7}$ は失敗
- ただし解けた素因数分解は素因数の情報を使ってる（[CRYPTREC](https://www.cryptrec.go.jp/exreport/cryptrec-ex-3005-2020.pdf) : それはありなのか）
- もっと大きい素因数分解に成功したものもあるがそれも全数探索 or 素数の性質を使ってる


# 共通鍵暗号への影響
## 攻撃モデル
- Q1 : 攻撃者は古典オラクルを使う（量子オラクルを使わない）
  - 公開鍵暗号はこちらのモデル
- Q2 : 攻撃者は量子オラクルを使う
  - 共通鍵暗号はこちらのモデルを使うことが多い（実際に攻撃できないことが多い）
## 共通鍵暗号の素朴な安全性評価
- 共通鍵暗号の鍵空間が $2^n$ なら古典では $O(2^n)$
- Groberのアルゴリズムを使う（Q2）と、$O(2^{n/2})$ で解読
- ハッシュ関数の衝突（$h(x)=h(x')$ となる $x\neq x'$）を求める問題
  - 古典 $O(2^{n/2})$ で解ける
  - Q2 : $O(2^{n/3})$ で解ける, ただし量子メモリは $O(2^{n/3})$ : 現実的でない → 当面大丈夫

# 用語のおさらい
## 耐量子計算機暗号(PQC : Post-Quantum Cryptography)
- 量子計算機が登場しても安全な、古典計算機上で動作する暗号 : 耐量子暗号とも
## 量子鍵配送（QKD : Quantum Key Distribution）
- 量子の性質を用いて秘密鍵を送信する途中で盗聴されたら検知できる : 仕組み : 量子暗号とも
## 暗号技術
- 共通鍵暗号 : 両者が同じ秘密情報を用いて暗号化・復号する方式
- ハッシュ関数 : 任意の長さのデータを固定長のデータに変換する関数
- 公開鍵暗号（PKC : Public Key Cryptography） : 公開情報と秘密情報を用いた仕組み
  - 公開鍵暗号方式（PKE : Public Key Encryption）
  - デジタル署名
  - ECDH鍵共有（KEM : Key Encapsulation Mechanisms, 鍵交換の一種）

# NISTのPQCプロセス
## 標準化スケジュール
- 2016 : NISTがPQCの標準化プロセスを開始
- 2017 : 69方式受理
- 2019 : 1st round : 26方式通過
- 2020 : 2nd round : 15方式通過
- 2022 : 3rd round : 4方式通過（PKEとKEMが標準方式に確定）
   - 保留だった4方式が4rd round評価へ
   - 2022/7 そのうちのSIKEが攻撃された
   - 署名は追加公募, 確定したものはドラフト作成中
- 2025 : 標準化文書公開

# PQC標準化の状況
## 確定したもの
- PKC/KEM : CRYSTALS-KYBER
- 署名 : CRYSTALS-Dilithium, FALCON, SPHINCS+
## 評価中
- PKC/KEM : BIKE, Classic McEliece, HQC
## 追加公募による1st round評価中
- 署名 : たくさん

# 主な暗号の種類
## 格子暗号
- CRYSTALS-KYBER(Kyber-768), FALCON
## ハッシュ関数
- SPHINCS+
## 符号暗号
- BIKE, Classic, McEliece, HQC
## 同種写像
- SIKE(PKC), SIDH(KEM) : 破れた / CSIDH, SQISign : 評価中, 現在有望と考えられている
## 多変数多項式
- 鍵サイズが大きい（公開鍵≧3MB, 秘密鍵≧400KB）

# 主なアルゴリズムの鍵サイズ
## 一覧

アルゴリズム|種類|公開鍵サイズ|暗号文・署名サイズ
---|---|---|---
ECDH|KEM|32B|32B
ECDSA|署名|32B|64B
Kyber-768 (MLKEM768)|KEM|1184B|1088B
Dilithium3|署名|1952B|3309B
SPHINCS+|署名|32B|7856B

## MLKEM768のブラウザ対応
- 2024/初め: Chrome 124/Edge/FirefoxがKyber-768対応
- 2025/9: iPhone (iOS26) のブラウザも対応
- [Cloudflare Research](https://pq.cloudflareresearch.com/) で確認できる

# 格子暗号
## LWE(Learning With Errors) 問題
- $𝔽_q$ 係数 $m \times n$ 次行列 $A$ と $s \in {𝔽_q}^n$ を選び $b:=A s+e \pmod{q}$ とする
$(A, b)$ が与えられたとき $s$ を求めよ
  - ここで $e$ は小さい整数からなる $m$ 次元縦ベクトル
  - $e=0$ なら（$m \ge n$ として）普通の連立方程式を解くので簡単
## より厳密には
- $\chi$: 平均0, 標準偏差 $σ$ の離散ガウス分布（整数 $x$ が $\exp(-x^2/2σ^2)$ に比例する確率）
  - $e$ は $\chi$ からサンプリングする
  - 厳密には通常の連続ガウス分布の結果を整数に丸めたものとは異なる
  - ただ

# NTRU問題
- 多項式 $f, g, F, G$ が $fG - gF \equiv q \pmod{x^n+1}$ を満たすとき
$h=gf^{-1} \bmod{(x^n+1,q)}$ からそれを満たす $f, g$ を求める問題
- 署名FALCONで利用

# 格子暗号の基本 Regev暗号
## 鍵生成
- $s \in (𝔽_q)^n$, $A$, $e$ をランダムに選び $b=As+e$ とする
  - $s$ が秘密鍵で $(A, b)$ が公開鍵
## $m\in [0, 1]$ の暗号化
- ベクトル $r$ をランダムに選び $u = A^T r$
- $v=b^T r + (q//2)m$ として $c=(u, v)$ が暗号文
## $c=(u, v)$ の復号
- $m=v-s^T u$ が 0 に近ければ $m=0$, そうでなければ $m=1$
## 正当性
- $m=(As+e)^T r+(q//2)m-s^T A^T r =e^T r + (q//2)m \approx (q//2)m$.

# 同種写像
## 従来のECDH鍵共有
- 楕円曲線の点 $P$ を固定
- AとBがそれぞれ $aP$, $bP$ を計算して共通な値 $abP$ を求める
## 同種写像
- 楕円曲線 $E$ を別の楕円曲線 $E'$ に移す写像 $\phi : E \rightarrow E'$.
- 複数の楕円曲線の間の同種写像を組み合わせて秘密鍵情報とする
- 同種写像問題
  - 与えらえた同種な楕円曲線 $E$, $E'$ の間の同種写像を具体的に求める
## SIDH（2022年破られた）
- $E_0$ から $E_A$, $E_B$ に移り、$E_{AB}$, $E_{BA}$ という楕円曲線を作る
- そこからj不変量という値を計算して鍵共有（$j(E_{AB})=j(E_{BA}$）する