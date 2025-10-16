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
- $E/𝔽_p$: 楕円曲線
- $G:=⟨P_0⟩=\Set{0,P_0,2 P_0,\dots, (r-1)P_0}$: 楕円曲線の点 $P_0$ の位数 $r$ の加法巡回群
乗法巡回群表記のテキストもある
- $G_T:=⟨μ⟩:=\Set{1,g,g^2,\dots, g^{r-1}} ⊆ 𝔽_{p^k}$:
$𝔽_p$ の $k$ 次拡大体の中の1の $r$ 乗根 $g$ からなる乗法巡回群
- $e:G × G → G_T$: ペアリングとは $e(a P_0, b P_0) = g^{ab}$ を満たすもの
## 双線型性
- $P, Q, R ∈ G$ に対して $P = a P_0, Q = b P_0, R = c P_0$ とすると
  - $e(P+Q, R) = e(P,R) e(Q,R) = g^{(a+b)c}$
  - $e(P, Q+R) = e(P,Q) e(P,R) = g^{a(b+c)}$
    - $G_T$ も加法群とみなすと通常の $f(x+y)=f(x)+f(y)$ の線型性の形
      - 2変数の両方に関して線型なので双線型

# ECDLPとペアリングの関係
## もともとはECDLPを解くために利用された
- $P, aP ∈ G$ が与えられたときに $a$ を求めたい
  - $g=e(P, P)$, $e(P, aP)=g^a$ なので $g$, $g^a$ に関するDLPが解ければECDLPも解ける
  - MOV (Menezes, Okamoto, Vanstone) リダクションという
## 3人の間の鍵共有 (Joux, 2000)
- A, B, C がそれぞれ秘密鍵 $a, b, c ∈ 𝔽_p$ を持つ
- $aP, bP, cP$ を共有する
- A は $e(bP, cP)^a$, B は $e(cP, aP)^b$, C は $e(aP, bP)^c$ を計算する
  - それぞれ $g^{abc}$ になるので鍵共有ができた
- より多数の鍵共有ができるか（多重線型写像の構成）は未解決（否定的な結果が優勢）
## BDDH (Bilinear DDH) 仮定
- $(P, aP, bP, cP, g')$ に対して $g' = e(P, P)^{abc}$ を判定する問題

# BLS署名
## 