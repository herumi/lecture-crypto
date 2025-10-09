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
# 耐量子計算機暗号
<br>
光成滋生, 2025/10

# 概要
## 量子計算機による暗号解読
- 素因数分解, 離散対数問題など重要な公開鍵暗号の安全性に関わる問題が破られる危険性
## 耐量子計算機暗号
- 耐量子暗号, PQC (Post-Quantum Cryptography) とも
- 量子計算機が登場しても安全な古典計算機で動作する暗号技術
## PQCへの移行
- 解読できなくても現在利用しているTLSを盗聴してデータを保存
- 将来量子計算機が登場したときに解読される危険性
- PQCへの移行は実用的な量子計算機の登場よりも前に進めるべき

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