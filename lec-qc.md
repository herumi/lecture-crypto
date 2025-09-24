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
## 粒子と波
- 粒子は1個, 2個と数えられる
- 粒子は同じ場所に複数個存在できない
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
  - 物理的に区別がつかない: 位相変換に対して不変という言い方をする

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
  - 基底$(|+\rangle, |-\rangle)$に従って $|0\rangle$ を観測すると $|+\rangle$ が得られる確率は $1/2$
  縫田光司『耐量子計算機暗号』p.182より引用

# 複数個のqubit
## テンソル積
- 2個の2次元ベクトルの基底を組み合わせて4次元ベクトル空間の基底を作る（合成系という）
  - 左のベクトルの各成分に右のベクトルを掛けて並べる（表記の都合で横ベクトルで表す）
  - $|00\rangle:=|0\rangle \otimes |0\rangle = (1,0) \otimes (1,0)=(1,0,0,0)$
  - $|01\rangle:=|0\rangle \otimes |1\rangle = (1,0) \otimes (0,1)=(0,1,0,0)$
  - $|10\rangle:=|1\rangle \otimes |0\rangle = (0,1) \otimes (1,0)=(0,0,1,0)$
  - $|11\rangle:=|1\rangle \otimes |1\rangle = (0,1) \otimes (0,1)=(0,0,0,1)$
  - 複素4次元ベクトル空間の基底
  - 一般に $c_{00}|00\rangle + c_{01}|01\rangle + c_{10}|10\rangle + c_{11}|11\rangle$ ($c_{ij} \in \mathbb{C}$, $\sum |c_{ij}|^2=1$) の形
  - この基底で観測したとき $|ij\rangle$ が得られる確率は $|c_{ij}|^2$
- 独立に準備された2個の1 qubit $|\psi_1\rangle$ と $|\psi_2\rangle$ がある状態を $|\psi_1\rangle \otimes |\psi_2\rangle$ と表す
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
  ![w:400px](images/lec-cnot1.drawio.svg) ![w:300px](images/lec-cnot2.drawio.svg)
  - 状態 $|x y\rangle$ ($x, y \in \Set{0,1}$) に対して $x=0$ のとき $y$ はそのまま, $x=1$ のとき $y$ は反転
  - $(x, y) \mapsto (x, x \oplus y)$ と表せる
- $x= \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$, $y=|0\rangle$ とすると $x \otimes y = \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle)$
  - $CNOT(x \otimes y)=\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$ となり量子もつれの状態になる
- 1 qubitの量子ゲートとCNOTゲートを組み合わせると任意のゲートを構成できる（定理）

# 量子計算機における計算
## $n$ qubitの状態
- $n$ bitのデータは $2^n$ 通りのパターンのどれか一つを表す
- $n$ qubitの状態は $2^n$ 通りのパターンが重なり合った状態を表す
  - $|\psi\rangle = \sum_{i=0}^{2^n-1} c_i |i\rangle$ ($c_i \in \mathbb{C}$, $\sum |c_i|^2=1$)
-


# 量子計算機の開発状況
## 誤り訂正
- 実際に計算できるためには誤り耐性量子計算（FTQC : Fault-Tolerant QC）が必要
- 実用的なものは100万 qubit程度必要と言われている

## 超伝導方式
- 2019 : Google 53 quibit
- [IBMのロードマップ](https://www.ibm.com/quantum/technology#roadmap)
  - 2021/11 : 127 qubit
  - 2022/11 : 433 qubit
  - 2023/12 : 1121 qubit Condor
    - 2023/12 : 日本は[64 quibit](https://resou.osaka-u.ac.jp/ja/research/2023/20231220_1)
    - 実際に動作確認は37 qubit?
# その他の方式
## イオントラップ方式
- 2023/6 : [IonQが29 quibit](https://ionq.com/posts/ionq-achieves-new-performance-milestone-of-29-algorithmic-qubits-aq-on-ionq)
  - 2024 : 35 quibitを目指す?
## 中性原子方式
- 2023/10 : [Atom Computing 1000 quibit](https://atom-computing.com/quantum-startup-atom-computing-first-to-exceed-1000-qubits/)
  - [48 論理 quibit 実現](https://www.nature.com/articles/s41586-023-06927-3)
## その他
- 電子, 光, マイクロ波 etc.
## 未来
- 2030/? 10~100万 qubit, 量子誤り訂正, 量子ランダムアクセス

# 量子計算機の復習
## 量子ビット（qubit）
- 量子計算機の基本単位
- 1qbitは $a|0 \rangle +b|1\rangle$ の形（$|\cdot\rangle$ はベクトルの基底, $a$, $b$ は複素数, $|a|^2+|b|^2=1$）
  - 観測すると $|a|^2$ の確率で $|0\rangle$ がえられる
- 2qbitだと $|00\rangle$, $|01\rangle$, $|10\rangle$, $|11\rangle$ の4つの基底の線形和（$|i\rangle\otimes |j\rangle=|ij\rangle$ : テンソル積）
  - $n$ qbitだと $2^n$ 個の状態を同時に扱える
    - $i$ 番目の状態（$i$を2進数展開して$|i_0 i_1 \cdots i_{n-1}\rangle$） $|i\rangle$ と表す
## 量子計算機の演算（ゲート）
  - $n$ qbitの状態を変換する演算を行列 $U$ で表す
  - $U$ は$2^n$ 次元のユニタリ行列（$U^\dagger U = UU^\dagger = I$, $\dagger$ は転置+複素共役）
  - 量子ゲートの入出力でqbitの数は変わらない（演算は可逆でなければならない）
  - 最後に観測したときに確率的にどれかの状態が現れる

# 量子計算機の計算
## 量子並列性
- 入力 $x=(x_i)$ に対する関数 $f(x)$ の計算
- $U_f : \sum_x |x\rangle\otimes |0\rangle \rightarrow \sum_x |x\rangle \otimes |f(x)\rangle$
  - $2^n$ 個の入力（$x=(x_i)$）に対して出力 $f(x_i)$ を同時に計算することを意味する
  - ただ, 観測したときどの $f(x_i)$ が出るかは確率的にしか決まらない
  - 望ましい $f(x_i)$ が観測されるように確率係数を大きくなる操作が必要
    - 量子計算機のアルゴリズムはそれをするためのもの

## 量子フーリエ変換
- $U|x\rangle=1/\sqrt{2^n} \sum_y \exp(2\pi ixy/2^n)|y\rangle$ を離散フーリエ変換DFTという
- ナイーブにDFTを実装すると $(2^n)^2$ ステップ必要
- うまい方法を使うと $O(n^2)$ 個の量子ゲート, $O(n^2)$ ステップで実現可能

# ショアのアルゴリズム
## 周期の探索
- $f(x) = g^x \bmod n$ のとき $f(x)=1$ となる $x$ を求める
  - もっと一般化された定式化があるが略
  - 古典なら $\log_2(n)$ の指数関数時間
  - 量子コンピュータなら $\log_2(n)$ の多項式時間
  - $U_f : |x\rangle \otimes |0\rangle \mapsto |x\rangle \otimes |f(x)\rangle$ として $U_f$ を構成し、DFTと組み合わせる

# RSA暗号の復習
## RSA暗号の肝
- 素数 $p, q$ を使って $n = pq$ を作る
- $ed \equiv 1 \pmod{(p-1)(q-1)}$ を満たす $e$（公開）, $d$（秘密） を作る
- $f(x,y) := x^y \bmod n$ として $f(f(m,e),d) \equiv m \pmod{n}$ を利用する
## RSA暗号の解読
- 適当な整数 $a$ に対して $a^r \equiv 1 \pmod{n}$ となる偶数 $r$ を探す
- $a^r-1=(a^{r/2}-1)(a^{r/2}+1) \equiv 0 \pmod{n}$
    - 因数のどちらかと $n$ の最大公約数を求めるとそれが $p$ か $q$ になる
    - ※を求める問題に帰着 → ショアのアルゴリズムで解読可能

# 楕円曲線暗号への影響
## 楕円曲線暗号の肝
- 楕円曲線の点 $P$ と整数 $x$（秘密）から $xP$（公開）を使って構成する暗号
- 楕円離散対数問題(ECDLP) : $xP$ と $P$ から $x$ は求められない
## 量子計算機による解読
- [ショアのアルゴリズムを適用してECDLPを解く](https://arxiv.org/abs/1706.06752)

## 量子計算機による解読見積もり（文献により差が大きい）
-|224 bit ECDLP|2048 bit RSA
-|---|---
Qubits|2042|6146 (20e+6)
gates|8.43e+10|3e+12 (5.20e+12)

# 現実
## 実際に解読できたパターン(by Wikipedia)
- 2001 IBM : 15 = 3x5
- 2012 [Josephson phase qubi](https://arxiv.org/abs/1202.5707) : 21 = 3x7
- 2019 IBM : 35を素因数分解しようとしたが失敗
- 2020 [NICT](https://www.nict.go.jp/press/2020/12/09-1.html) : $2^x\equiv 1 \pmod{2}$ は解けたが $4^x \equiv 2 \pmod{7}$ は失敗
- ただし解けた素因数分解は素因数の情報を使ってる（[CRYPTREC](https://www.cryptrec.go.jp/exreport/cryptrec-ex-3005-2020.pdf) : それはありなのか）
- もっと大きい素因数分解に成功したものもあるがそれも全数探索 or 素数の性質を使ってる
## 感想
- 量子コンピュータの進展の割に10年以上記録が更新されていないのは何故?
- [ショアのアルゴリズムでは素因数分解できない](https://arxiv.org/abs/2306.10072)と主張する人もいる
（査読あり学会には通っていない模様）

# グローバーの探索アルゴリズム
## $N$個のデータから特定のパターンにマッチするものを探す問題
- $[0, N-1]$ 上の関数で, $f(a)=1 \text{ if } x = a$, otherwise $f(x)=0$ なるものを考える
  - 仮定 : $f(x)$ の計算も量子コンピュータが行う（量子オラクル）
  - $f(x)$ の計算ステップは無視している
- 古典計算機なら $x=a$ を求めるのに平均 $N/2$ 回の試行が必要
- グローバーのアルゴリズムなら $O(\sqrt{N})$ 回の試行でOK
  - 量子ビットは $O(\log N)$ 必要
  - $U_f$ をうまく構成して1回ごとに $x=a$ となる確率だけ大きくして,
  他は小さくなるようにする
    - $|a\rangle$ でだけ反転, それ以外はそのままの写像と別の写像との組み合わせの繰り返し
  - $O(\sqrt{N})$ 回の試行で $x=a$ となる確率が $1-1/N$ になる（※）

# サイモンのアルゴリズム
## 周期の探索
- $f : [0, 1]^n → [0, 1]^n$ が, ある $r \in [0, 1]^n \setminus 0$ が存在して $f(x \oplus r) = f(x)$ が成り立つとき,
$r$ を求めよ
  - $O(n \log n)$ で求められる

# 共通鍵暗号への影響
## 攻撃モデル
- Q1 : 攻撃者は古典オラクルを使う（量子オラクルを使わない）
  - 公開鍵暗号はこちらのモデル
- Q2 : 攻撃者は量子オラクルを使う
  - 共通鍵暗号はこちらのモデルを使うことが多い（実際に攻撃できないことが多い）
## 共通鍵暗号の素朴な安全性評価
- 共通鍵暗号の鍵空間が $2^n$ なら古典では $O(2^n)$
- グローバーのアルゴリズムを使う（Q2）と、$O(2^{n/2})$ で解読
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
Kyber-768|KEM|1184B|1088B
Dilithium3|署名|1952B|3309B
SPHINCS+|署名|32B|7856B

## ブラウザ対応
- 2024/初め : Chrome 124/Edge/FirefoxがKyber-768対応

# 格子暗号
## LWE(Learning With Errors)問題の困難性
- $𝔽_q=\Set{0, \dots, q-1}$, 行列 $A$, ベクトル $b$ が与えられたときに $x \in (𝔽_q)^n$ に関する方程式 
$A x=b+e \pmod{q}$ を解くのが難しい
  - ここで $e$ は小さいノイズ（$e_i \in [-1,1]$）
  - $e=0$ なら普通の連立方程式で解くのは簡単
## NTRU問題
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