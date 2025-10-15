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
## type-1ペアリング
- $E/𝔽_p$: 楕円曲線
- $G:=⟨P_0⟩=\Set{0,P_0,2 P_0,\dots, (r-1)P_0}$: 楕円曲線の点 $P_0$ の位数 $r$ の加法巡回群
乗法巡回群表記のテキストもある
- $G_T:=⟨μ⟩:=\Set{1,μ,μ^2,\dots, μ^{r-1}} ⊆ 𝔽_{p^k}$:
$𝔽_p$ の $k$ 次拡大体の中の1の $r$ 乗根 $μ$ からなる乗法巡回群
- $e:G × G → G_T$: ペアリングとは $e(a P_0, b P_0) = μ^{ab}$ を満たすもの
## 双線型性
- $P, Q, R \in G$ に対して $P = a P_0, Q = b P_0, R = c P_0$ とすると
  - $e(P+Q, R) = e(P,R) e(Q,R) = μ^{(a+b)c}$
  - $e(P, Q+R) = e(P,Q) e(P,R) = μ^{a(b+c)}$