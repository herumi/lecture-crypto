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
光成滋生, 2025/10

# 概要
## 古典計算機
- 現在（古典）計算機はビット (0 or 1) を基本単位として計算
- 論理ゲート: AND, OR, NOTなどのビット演算の組合せ
## 量子計算機 QC (Quantum Computer)
- 量子力学で記述される現象を利用した新しい計算機
  - 攻撃: 量子計算機を利用して暗号技術を破る量子アルゴリズム
  - 対策: 耐量子計算機暗号（量子計算機が登場しても安全な現在の計算機で実行できる暗号）
  - 量子鍵配送（量子暗号）: 量子の性質を利用した秘密鍵を共有する技術
## 粒子と波
- 粒子は1個, 2個と数えられ, 同じ場所に複数個存在できない
- 波は数えられない広がりを持った状態
- 複数の波が重なり合って干渉する

# 量子計算機
<!-- _class: image-right -->
![w:500px](images/lec-qc1.drawio.svg)
## 量子の性質を利用した計算機
- 量子: 粒子と波の両方の性質を持ったもの
- 0の状態を$|0\rangle$, 1の状態を$|1\rangle$と表す
- 量子ビット (qubit) : QCの基本単位
  - qubit : $|\psi\rangle:=a|0\rangle + b|1\rangle$
    - $a, b \in ℂ$, $|a|^2+|b|^2=1$
    - $(|0\rangle, |1\rangle)$ は複素2次元ベクトル空間の基底
## 観測
- $|\psi\rangle$ を基底 $(|0\rangle, |1\rangle)$ に従って「観測」すると
$|a|^2$ の確率で $|0\rangle$, $|b|^2$ の確率で $|1\rangle$ が得られるという原理
  - $θ$ を実数として $|\psi'\rangle:=e^{iθ} |\psi\rangle$ を観測しても同じ確率（$|e^{iθ}|=1$ なので）
  - $|\psi\rangle$ と $|\psi'\rangle$ は物理的に区別がつかない: $e^{iθ}$ を位相因子, 位相変換に対して不変という

# 線形代数の復習
## ユニタリ行列の定義と性質
- $U^\dagger U = I$ を満たす複素行列 $U$ をユニタリ行列という（$I$ は単位行列）
  - $U^\dagger$ は $U$ の「転置＋複素共役」（$U=(u_{ij})$ なら $U^\dagger=(\overline{u_{ji}})$）を表す
- $U$ がユニタリ行列なら $U^{-1}=U^\dagger$ なので $U$ は可逆
- ユニタリ行列はベクトルの長さを変えない
  - $v$ が $|v|=1$ なら $1=v^\dagger v=v\dagger (U^\dagger U) v=(Uv)^\dagger (Uv)=|Uv|^2$ なので $|Uv|=1$
## 固有値と固有ベクトル
- $A$: 行列, $v$: ベクトル, $λ \in ℂ$ について $Av=λv$ を満たすとき $v$: $A$ の固有ベクトル, $λ$: 固有値
- $A$ がユニタリ行列のとき $|v|=1$ とすると $|v|=|Av|=|λ||v|$ なので $|λ|=1$
  - ユニタリ行列の固有値は絶対値が1の複素数なので $λ=e^{iθ}$ ($θ \in ℝ$) と表せる
# 量子ゲート
## qubitの状態を変換する演算
- $|0\rangle$ を $\begin{pmatrix}1 \\ 0\end{pmatrix}$, $|1\rangle$ を $\begin{pmatrix}0 \\ 1\end{pmatrix}$ と表すと $|\psi\rangle$ を $a|0\rangle + b|1\rangle=\begin{pmatrix}a \\ b\end{pmatrix}=:v$ と表現できる
  - $|v|=|a|^2 + |b|^2=1$ なので $v$ は単位ベクトル
- 複素2次元ベクトル $\begin{pmatrix}a \\ b\end{pmatrix}$ にユニタリ行列 $U$ を掛ける操作を量子ゲートという
  - ユニタリ行列はベクトルの長さを変えないので $Uv$ もqubitの状態を表す
- ユニタリ行列は可逆なので量子ゲートは可逆な変換しかできない
  - 例えば古典の AND ゲートは不可逆なので量子ゲートでは実現できない
  - 後述する複数のqubitを用いて $(x,y,z) \mapsto (x, y, z \oplus (x \land y))$ のような形で実現する

# 量子ゲートの例
## 代表的な量子ゲート
- X (NOT) ゲート: $X:=\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}$
  - $X|0\rangle = |1\rangle$, $X|1\rangle = |0\rangle$: 基底の反転
- アダマールゲート: $H:=\frac{1}{\sqrt{2}}\begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}$
  - $H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$, $H|1\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$
  - $|+\rangle := H|0\rangle$, $|-\rangle := H|1\rangle$ と表記することが多い
- 位相回転: $R(θ):=\begin{pmatrix}1 & 0 \\ 0 & e^{iθ}\end{pmatrix}$
  - $R(θ)|0\rangle = |0\rangle$, $R(θ)|1\rangle = e^{iθ}|1\rangle$
  - $|1\rangle$ の位相を $θ$ だけ回転させる
  - $T:=R(π/4)$, $S:=R(π/2)$ と略記することが多い（$T^2=S$）

# 異なる基底での観測
## 相互関係
- $|+\rangle= \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$, $|-\rangle= \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$
- $|0\rangle=\frac{1}{\sqrt{2}}(|+\rangle + |-\rangle)$, $|1\rangle=\frac{1}{\sqrt{2}}(|+\rangle - |-\rangle)$
## 基底を取り替えて観測する
- $(|0\rangle, |1\rangle)$ 以外の基底で観測できる
- $(|+\rangle, |-\rangle)$ も別の基底なので $|+\rangle, |-\rangle$ で観測してみる
- $|0\rangle$ を $(|0\rangle, |1\rangle)$ に関して観測すると確率 $1$ で $|0\rangle$
- $|0\rangle$ を $(|+\rangle, |-\rangle)$ に関して観測すると確率 $1/2$ で $|+\rangle$ か $|-\rangle$
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
- 一般に $\cal H$ の元は $c_{00}|00\rangle + c_{01}|01\rangle + c_{10}|10\rangle + c_{11}|11\rangle$ ($c_{ij} \in ℂ$, $\sum |c_{ij}|^2=1$) の形
  - この基底で観測したとき $|ij\rangle$ が得られる確率は $|c_{ij}|^2$
- $n$個のqubitの状態は $2^n$ 次元複素ベクトルとなる
  - $|i_0 i_1 \cdots i_{n-1}\rangle$ を $i$ を2進数展開($i=\sum_k i_k 2^k$) したものとみなして $|i\rangle$ と略記する
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
  - 2個のqubitは離れた状態でも成り立つ（量子テレポーテーションの原理）

# CNOT (Controlled NOT) ゲート
## 2個のqubitに対する量子ゲート
- $CNOT(a|00\rangle + b|01\rangle + c|10\rangle + d|11\rangle):=a|00\rangle + b|01\rangle + d|10\rangle + c|11\rangle$
  - 後ろ2個の基底の係数が入れ代わる
  ![w:400px](images/lec-cnot1.drawio.svg) ![w:600px](images/lec-cnot2.drawio.svg)
  - 状態 $|x y\rangle$ ($x, y \in \Set{0,1}$) に対して $x=0$ のとき $y$ はそのまま, $x=1$ のとき $y$ は反転
  - $(x, y) \mapsto (x, x \oplus y)$ と表せる
- $x= \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$, $y=|0\rangle$ とすると $x \otimes y = \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle)$
  - $CNOT(x \otimes y)=(1/\sqrt{2})(|00\rangle + |11\rangle)$ となり量子もつれの状態になる
- $H$, $T$, CNOT の組合せで任意の量子ゲートを近似できる（量子計算の普遍性）
  - これら（と $S=T^2$ も追加して）を使って量子回路を組み立てる

# 2qubitに対するアダマールゲート
## $H \otimes H = H^{\otimes 2}$ と表記
- $H=(1/\sqrt{2})\pmatrix{1 & 1 \\ 1 & -1}$ なので
  - $H^{\otimes 2} |00\rangle = \frac{1}{2}(|00\rangle + |01\rangle + |10\rangle + |11\rangle)$
  - $H^{\otimes 2} |01\rangle = \frac{1}{2}(|00\rangle - |01\rangle + |10\rangle - |11\rangle)$
  - $H^{\otimes 2} |10\rangle = \frac{1}{2}(|00\rangle + |01\rangle - |10\rangle - |11\rangle)$
  - $H^{\otimes 2} |11\rangle = \frac{1}{2}(|00\rangle - |01\rangle - |10\rangle + |11\rangle)$
- $H^{\otimes 2} |i \rangle = \frac{1}{2} \sum_{j=0}^{3} (-1)^{i \cdot j} |j\rangle$ ($i=0,1,2,3$)
  - $i \cdot j$ は $i, j$ を2進数展開したときの各桁の積の和（$\bmod{2}$）
  - 例えば $i=2=10_2$, $j=3=11_2$ のとき $i \cdot j = 1 \times 1 + 0 \times 1 = 1$
- $H^{\otimes n} |i\rangle = (1/2^{n/2})\sum_{j=0}^{2^n-1} (-1)^{i \cdot j} |j\rangle$ ($i=0,1,\dots,2^n-1$)

# 量子計算機における計算
<!-- _class: image-right-center -->
![w:470px](images/lec-qc-algo.png)
## $n$ qubitの状態
- $n$ qubitの状態は $2^n$ 通りのパターンが重なり合った状態
  - $|\psi\rangle = \sum_{i=0}^{2^n-1} c_i |i\rangle$ ($c_i \in ℂ$, $\sum |c_i|^2=1$)
## 量子計算機の演算処理
- $|\psi\rangle$ に量子ゲート（ユニタリ行列）を順番に作用させる
  - 原理的に1回で最大 $2^n$ 個のパターンを処理可能
- 最終的には観測しないと結果を得られない
  - そのとき $|c_i|^2$ の確率で $|i\rangle$ に確定し, これが計算結果
  - もし $|c_0| = \dots = |c_{2^n-1}|$ ならどの $|i\rangle$ が得られるか完全にランダム
- 望ましい答えが観測されるように $|c_i|$ を大きくするのが量子アルゴリズムの肝
  - 古典計算機における分岐・ループ処理は存在しない
  - 基本的に10回ループする処理は10個の量子ゲートを並べる必要がる
  （古典の手作り回路にイメージが近い）
# 一般の関数に対する量子ゲート
## 補助ビット (ancilla) の導入
- 関数 $f : \Set{0,1}^n \to \Set{0,1}$ に対して
$U_f : |x\rangle \otimes |y\rangle \mapsto |x\rangle \otimes |y \oplus f(x)\rangle$ と定義する
  - $x$: $n$ qubit, $y$: 1 qubit （$y$ が補助ビット）
- このとき $U_f$ はユニタリ行列になる
  - $U_f(U_f(|x\rangle \otimes |y\rangle)) = |x\rangle \otimes |y \oplus f(x) \oplus f(x)\rangle = |x\rangle \otimes |y\rangle$, つまり $U_f^{-1} = U_f$
- 位相キックバック
  - $|y\rangle:=|-\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$ とする
    - $f(x)=0$ のとき $U_f(|x\rangle \otimes |-\rangle) = |x\rangle \otimes |-\rangle$
    - $f(x)=1$ のとき $U_f(|x\rangle \otimes |-\rangle) = -|x\rangle \otimes |-\rangle$
    - つまり $U_f(|x\rangle \otimes |-\rangle) = (-1)^{f(x)} |x\rangle \otimes |-\rangle$
    $f(x)$ を位相部分に埋め込む演算 $U_f(|x\rangle)=(-1)^{f(x)}|x\rangle$ とみなす

# Groverのアルゴリズム
## $N$ 個のデータから特定の条件を満たすものを一つ探す
- 関数 $f(x) = 1$ if $x=a$, それ以外は0 において $f(x)=1$ となる $x=a$ を探す
- 古典計算機なら平均 $N/2$ 回の試行が必要
- Groverのアルゴリズムは $O(\sqrt{N})$ 回の量子クエリで可能
  - $O(\sqrt{N})$ 回のクエリで十分高い確率で $f(x)=1$ なる $x$ が見つかるということ
![w:700px](images/lec-grover.png)

# Shorのアルゴリズム
## $n=pq$ ($p$, $q$ は素数) を素因数分解するアルゴリズム
- 位数計算問題: 与えられた $g \in [1, n-1]$ の位数を求める問題
  - $g$ の位数: $g^r \equiv 1 \pmod{n}$ となる最小の正整数
- 位数が見つかり $r$ が偶数ならば $(g^{r/2} - 1)(g^{r/2} + 1) \equiv 0 \pmod{n}$
  - このとき有意な確率で $g^{r/2}-1$ と $g^{r/2}+1$ のどちらかは $n$ の非自明な約数を持つ
  - 見つからなければ別の $g$ でやり直す
  - 最大公約数は古典計算機で高速に求められるので $p, q$ が得られる

- 位数計算問題を量子計算機で解き, 全体で $O((\log n)^3)$ で素因数分解できる

# QFT (Quantum Fourier Transform)
## 量子フーリエ変換
- 古典フーリエ変換の量子版
- $n$ qubit の $|x\rangle = \sum_{j=0}^{N-1} x_j | j\rangle$, $N:=2^n$
- QFTは $|j\rangle$ を $\frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} \exp(2 π i j k / N) |k\rangle$ に変換する（$|j\rangle$ という状態と位相の相互変換）

  - $O(n^2)$ 個の量子ゲート, $O(n^2)$ ステップで実現可能
## 古典FFT
- $x_k$ を $X_j := (1/\sqrt{N})\sum_{k=0}^{N-1} x_k \exp(-2 π i j k / N)$  に変換する
- 逆変換は $x_k = (1/\sqrt{N}) \sum_{j=0}^{N-1} X_j \exp(2 π i j k / N)$
- $x_l = (1/\sqrt{N}) \sum_{j=0}^{N-1} X_j \exp(2 π i j l / N)= (1/N) \sum_{j,k} x_k \exp(2 π i j (l-k) / N)$
  - $\sum_j \exp(2 π i j (l-k) / N) = N$ if $l=k$, else $0$

# 量子位相推定 QPE (Quantum Phase Estimation)
## ユニタリ行列 $U$ の固有値を求める
- $U$ の固有値は絶対値が 1 なので $e^{2 π i θ}$ ($θ \in [0,1)$) と表せる
- $U$ の固有ベクトル $|\psi\rangle$ が与えられたとき $U|\psi\rangle = e^{2 π i θ} |\psi \rangle$ となる $θ$ を $m$ 桁の精度で求める
## 大まかな手順
- $|0^{\otimes m}\rangle$ にアダマールゲートを作用させて $(1/2^{m/2}) \sum_{k=0}^{2^m-1} |k\rangle$ を作る
- $U^k$ を作用: $|k\rangle \mapsto \exp(2π i k θ)|k\rangle$
  - 結果: $(1/2^{m/2}) \sum_{k=0}^{2^m-1} e^{2 π i k θ} |k\rangle \otimes |\psi\rangle$
- 逆QFTを作用: $|k\rangle \mapsto (1/2^{m/2}) \sum_{j=0}^{2^m-1} \exp(-2 π i j k / 2^m) |j\rangle$
  - 結果: $(1/2^m) \sum_{k,j} \exp(2 π i k (2^m θ - j)/2^m) |j\rangle \otimes |\psi\rangle$
- 測定:
  - ある $j$ について $2^m θ=j$ なら $|j\rangle |\psi\rangle$ なので $j$ が求まる
  - $θ \approx j/2^m$ なら40%程度の確率で $|j\rangle |\psi\rangle$ になる

# QPEを用いた位数計算の概略
## 演算 $U|x\rangle := |g x \bmod n\rangle$
- このとき $U |j\rangle = \exp(2 π i j / r) |w_j\rangle$
$|w_j\rangle := (1/\sqrt{r}) \sum_{k=0}^{r-1} \exp(-2 π i j k / r) |g^k \bmod n\rangle$ となることが知られている
- 固有値に $j/r$ が含まれている
- QPEにより $j/r$ の近似値が求まる
  - $(1/\sqrt{r})\sum_j |w_j\rangle = |1\rangle$ なので $|1\rangle$ に対してQPEを適用しても位相が求まる
  - 連分数展開の技法を使って正確な値を求める
- $U^{2^k}|x\rangle = |g^{2^k} x \bmod n\rangle$ なので $g^{2^k} x \bmod n$ を事前計算する

# 量子計算機 QCとECDLP
## ECDLPからHSPへの帰着
- $S:=\langle P \rangle$ を $𝔽_p$ 上の楕円曲線の素数位数 $n$ の巡回群とする.
ECDLP: $Q \in S$ に対して $Q=kP$ となる $k$ を見つける問題
- $|0,0\rangle|0\rangle$ にアダマールゲートを作用させて $(1/n)\sum_{a,b}|a,b\rangle|0\rangle$ を作る
- $U|a,b\rangle|0\rangle := |a,b\rangle|aP + bQ\rangle$ を作用させる
  - 結果: $(1/n)\sum_{a,b}|a,b\rangle|aP + bQ\rangle$
- 逆QFTを作用させて測定してある点 $R$ が観測される
  - 結果 $(a,b)$, $(a',b') \in S_R:=\Set{(a,b)\mid aP + bQ = R}$
- $O((\log p)^3)$ で解けることが知られている
- ビット数が少ない分, 原理的に素因数分解よりも効率よく求められる

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
- qubitを増やすだけでなくエラー率の低減・運用コストなども課題

# 量子計算機の実装例
## 超伝導方式
- Google: 2019年 53 qubit, 2024年 105 qubit
- [IBMのロードマップ](https://www.ibm.com/quantum/technology#roadmap): 2021年 127 qubit, 2022年 433 qubit, 2023年 1121 qubit Condor
- 大阪大学: 2023年 [64 quibit](https://resou.osaka-u.ac.jp/ja/research/2023/20231220_1), 富士通と理研: 2025年 [256 qubit](https://pr.fujitsu.com/jp/news/2025/04/22.html)
## イオントラップ方式
- 2023/6: [IonQが29 quibit](https://ionq.com/posts/ionq-achieves-new-performance-milestone-of-29-algorithmic-qubits-aq-on-ionq), 2025: Quantinuum 56 qubit
- 2025/6: [1qubitで1/670万のエラー率](https://qiqb.osaka-u.ac.jp/newstopics/pr20250623)

## 中性原子方式
- 2023/10: Atom Computing [1180 quibit](https://atom-computing.com/quantum-startup-atom-computing-first-to-exceed-1000-qubits/)
- 2025/9: [6100 qubit, 0.02%のエラー率](https://www.caltech.edu/about/news/caltech-team-sets-record-with-6100-qubit-array)

- その他: 電子, 光, マイクロ波 etc.

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
- PKC/KEM : CRYSTALS-KYBER, [HQC](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8545.pdf) (2025/3確定 2027年標準化予定)
- 署名 : CRYSTALS-Dilithium, FALCON, SPHINCS+

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
MLKEM768 (KYBER-768)|KEM|1184B|1088B
Dilithium|署名|1952B|3309B
SPHINCS+|署名|32B|7856B

## MLKEM768のブラウザ対応
- 2024/初め: Chrome 124/Edge/FirefoxがKyber-768対応
- 2025/9: iPhone (iOS26) のブラウザも対応
- [Cloudflare Research](https://pq.cloudflareresearch.com/) で確認できる

# 格子暗号
## LWE(Learning With Errors) 問題
<!-- _class: image-right -->
![w:400px](images/lec-lwe.drawio.svg)
- $M_{m,n}(𝔽_q)$ を縦 $m$, 横 $n$ の $m \times n$ 次行列全体の集合とする
  - 行列や
- $A \in M_{m,n}(𝔽_q)$ と縦（列）ベクトル $s \in {𝔽_q}^n$ を選ぶ
$b:=A s+e \pmod{q}$ とし, $(A, b)$: givenのとき $s$ を求めよ
  - ここで $e$ は小さい整数（後述）からなる $m$ 次元縦ベクトル
  - $e=0$ なら（$m \ge n$ として）普通の連立方程式を解くだけ
## 仮定
- 適切なパラメータに対してLWE問題は困難であることをLWE仮定という
- （判定版）LWE仮定
  - 上記の方法で生成した $\Set{(A, b)}$ を（計算）LWE分布という
  - LWE分布と $(A, b) \underset{U}\leftarrow M_{m,n}(𝔽_q) \times {𝔽_q}^m$ を区別するのが困難

# ノイズの分布
<!-- _class: image-right -->
## 連続ガウス分布
![w:400px](images/lec-gauss.drawio.svg)
- 平均0, 標準偏差 $σ$ のガウス分布
  - $P(x) = \frac{1}{\sqrt{2π}σ} \exp(-x^2/2σ^2)$
## 離散ガウス分布
- 整数 $x$ が $\exp(-x^2/2σ^2)$ に比例する確率で分布する
  - $e$ は離散ガウス分布からサンプリングする
- 厳密には通常の連続ガウス分布の結果を整数に丸めたものとは異なる
- 扱いが困難なので実装時には適当なパラメータ $L$ を決めて $[-L, L]$ の範囲で生成する

# Regev暗号
## 鍵生成
- $s \in {𝔽_q}^n$, $A \in M_{m,n}(𝔽_q)$, $e \in {𝔽_q}^m$ を選び $b:=As+e$ とする
  - $s$ が秘密鍵で $(A, b)$ が公開鍵
## $m\in \Set{0, 1}$ の暗号化
- $r \underset{U}\leftarrow \Set{0,1}^m$ を選び $c:=(A^T r, b^T r + (q//2)m)$ が暗号文 ($q//2:=\texttt{floor}(q/2)$)
## $c=(u, v)$ の復号
- $m:=[v-s^T u]_q$ が 0 に近ければ $m=0$, そうでなければ $m=1$
  - ここで $[a]_q$ は $a \in [0, q-1]$ を $a \le q//2$ なら $a$, それ以外は $a-q//2$ とする
## 正当性
- $m=(As+e)^T r+(q//2)m-s^T A^T r =e^T r + (q//2)m \approx (q//2)m$
  - $e^T r \ll (q//2)$ なら正しく復号できる

# 構造化格子
## 多項式環上の格子
- データサイズ削減のためにより効率のよい格子を利用する
- $q$: 素数, $n$: 2のべき, 1の原始 $ν$ 乗根 $ζ \in 𝔽_q$ （位数が $ν$: $ζ^ν=1$）
  - MLKEM768では $q=3329$, $n=256$, $ν=256$, $ζ=17$
- $\phi(x):=x^n+1$, $R:=ℤ[x]/(x^n+1)$, $R_q:=𝔽_q[x]/(x^n+1)$
## MLWE (Module LWE) 問題
- $s \underset{U}\leftarrow {R_q}^k$ とノイズの分布 $χ$ を選ぶ（$s \cdot a$ は2個の $k$ 次元ベクトルの内積）
MLWE分布: $A_{s,χ}:=\Set{(a,s \cdot a + e) \in {R_q}^k \times R_q \mid a \underset{U}\leftarrow {R_q}^k, e \leftarrow χ}$

## MLWE仮定
- MLWE分布と $(a,b) \underset{U}\leftarrow {R_q}^k \times R_q$ を区別するのが困難
# MLKEM768
## パラメータ
- $m = O(n \log q)$
- q = 3329, n = 256, k = 3, η = 2
- $e$ は $n=4$, $p=1/2$ の二項分布（範囲は  $[-2, 2]$）を利用

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