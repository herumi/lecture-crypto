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
# ペアリング暗号
<br>
光成滋生, 2025/10
<br>

# 概要
## 目的
- ペアリングの性質, BLS署名の理解

# ペアリング
## type-1ペアリング (Weil pairing)
- $E/𝔽_p$: 楕円曲線, $G_1:=⟨P_1⟩=\Set{0,P_1,2 P_1,\dots, (r-1)P_1}$: 位数 $r$ の加法巡回群
乗法巡回群表記のテキストもある
- $G_T:=⟨g⟩:=\Set{1,g,g^2,\dots, g^{r-1}} ⊆ 𝔽_{p^k}$: 1の $r$ 乗根 $g$ からなる乗法巡回群
- $e:G_1 × G_1 → G_T$ がペアリングとは $e(a P_1, b P_1) = g^{ab}$ を満たすもの
## 双線型性
- $P, Q, R ∈ G_1$ に対して $P = a P_1, Q = b P_1, R = c P_1$ とすると
  - $e(P+Q, R) = e(P,R) e(Q,R) = g^{(a+b)c}$
  - $e(P, Q+R) = e(P,Q) e(P,R) = g^{a(b+c)}$
    - $G_T$ も加法群とみなすと通常の $f(x+y)=f(x)+f(y)$ の線型性の形
      - 2変数の両方に関して線型なので双線型

# ECDLPとペアリングの関係
## もともとはECDLPを解くために利用された
- $P, aP ∈ G_1$ が与えられたときに $a$ を求めたい
  - $g=e(P, P)$, $e(P, aP)=g^a$ なので $g$, $g^a$ に関するDLPが解ければECDLPも解ける
  - MOV (Menezes, Okamoto, Vanstone) リダクションという
## 3人の間の鍵共有 (Joux, 2000)
- A, B, C がそれぞれ秘密鍵 $a, b, c ∈ 𝔽_r$ を持ち $aP, bP, cP$ を共有する
- A は $e(bP, cP)^a$, B は $e(cP, aP)^b$, C は $e(aP, bP)^c$ を計算する
  - それぞれ $g^{abc}$ になるので鍵共有ができた
- より多数の鍵共有ができるか（多重線型写像の構成）は未解決（否定的な結果が優勢）
## 主な安全性仮定の問題
- CBDH (Computational Bilinear DH): $(P, aP, bP, cP)$ に対して $e(P, P)^{abc}$ を計算する
- DBDH (Decisional BDH): $(P, aP, bP, cP, g')$ に対して $g' = e(P, P)^{abc}$ を判定する

# BLS署名
## CBDH仮定の元で安全な署名
- Boneh, Lynn, Shacham (2001)
  - $H:\Set{0,1}^* → G_1$ をハッシュ関数
- KeyGen: 秘密鍵: $s \underset{U}← 𝔽_r$, 公開鍵 $P := s P_1$
- Sign: メッセージ $m$ に対して $σ := s H(m)$
- Verify: $e(H(m), P) = e(σ, P_1)$ ならvalid
  - 正当性: $\text{LHS} = e(H(m), s P_1) = e(s H(m), P_1) = \text{RHS}$
## 特徴
- 署名長が短い（$G_1$ の要素1個）, 乱数不要の決定的アルゴリズム
- 公開鍵と署名がどちらも「秘密鍵 × $G_1$ の元」の形

# type-3ペアリング
## ペアリングの重要性と高速化の必要性
- ペアリングの重要性に伴いより効率のよい写像が望まれている
- 現在の主流は非対称ペアリング
 $e:G_1 × G_2 → G_T$: で$G_1 ≠ G_2$ かつ $G_1$ と $G_2$ の間に効率的な同型写像が存在しない

## BLS12-381曲線 (Barreto, Lynn, Scott)
  - BLS写像のBLSとは無関係
  - $E/𝔽_p$: $y^2 = x^3 + 4$ （$p$: 381bit素数）
  - 写像先の $G_T ⊆ 𝔽_{p^{12}}$ は $𝔽_p$ の $k=12$ 次拡大体（BLS12の12）
  - $G_1 := ⟨P_1⟩ ⊆ E(𝔽_p)$: $P_1$ の位数は255bit素数 $r$
  - $G_2 := ⟨P_2⟩ ⊆ E'(𝔽_{p^2})$: 2次拡大体上の楕円曲線 $E': y^2=x^3+4(1+i)$, $i^2=-1$
  - $G_T=⟨g⟩=⟨e(P_1,P_2)⟩$
  $e:G_1 × G_2 → G_T$: $e(a P_1, b P_2) = e(P_1, P_2)^{ab}=g^{ab}$ を満たす

# type-3ペアリングでのBLS署名
## type-1版をtype-3版に適用する
- $G_i:=⟨P_i⟩$, $H_i:\Set{0,1}^* → G_i$ ($i=1,2$): ハッシュ関数, $b ∈ \Set{1,2}$ を固定
- 秘密鍵: $s \underset{U}← 𝔽_r$ に対して
  - $b=1$ のとき 公開鍵 $P := s P_1 ∈ G_1$, 署名 $σ := s H_2(m) ∈ G_2$
    - 検証: $e(P, H_2(m)) = e(P_1, σ)$ ならvalid
  - $b=2$ のとき 公開鍵 $P := s P_2 ∈ G_2$, 署名 $σ := s H_1(m) ∈ G_1$
    - 検証: $e(H_1(m), P) = e(σ, P_2)$ ならvalid
- 公開鍵が小さい方がよいなら $b=1$, 署名が小さい方がよいなら $b=2$
## 安全性仮定
- co-CDH仮定: $P_1, a P_1∈G_1, P_2∈G_2$ に対して $a P_2$ が計算困難（$b=2$ も同様）

<!--
- SXDH (Symmetric external DH)
  - $G_1$, $G_2$ それぞれのDDHが難しい
  - 派生物の仮定がいろいろある
-->