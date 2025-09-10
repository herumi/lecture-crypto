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
# 公開鍵暗号
<br>
光成滋生
<br>

# DH (Diffie-Hellman) 鍵共有
## 盗聴者のいる通信経路で安全に通信する方法
### AとBの間の鍵共有
- $p$: 素数, $g$: 0でない整数 ($0 < g < p$) を選び $p$ と $g$ を共有する（public）
- A は $x \in [1, p-1]$ をランダムに選んで $X:=g^x \bmod{p}$ （$p$ で割った余り）を B に送る
- B は $y \in [1, p-1]$ をランダムに選んで $Y:=g^y \bmod{p}$ を A に送る
- A は $s_1=Y^x \bmod{p}$, B は $s_2=X^y \bmod{p}$ を計算する
![w:600px](images/lec-dh1.drawio.svg)

# これでうまくいくのか?
## $s_1=s_2=s$
- 整数 $a$, $b$ に対して $(a \bmod{p}) \times (b \bmod{p}) \bmod{p} = (a \times b) \bmod{p}$
- よって $a^b \bmod{p} = (a \bmod{p})^b \bmod{p}$
- $s_1=Y^x \bmod{p} = (g^y \bmod{p})^x \bmod{p} = (g^y)^x \bmod{p} = g^{xy} \bmod{p} = s_2$
  - 以降、煩雑なので $\bmod{p}$ は省略する
## 安全なのか?
- 盗聴者は $p$, $g$, $X$, $Y$ を盗聴できる
- 盗聴者はこれらの情報から $s$ を計算できるか?
- $X=g^x$ が分かっているのだから、$g$, $g^2$, $g^3$, ... と計算して $X=g^x$ となる $x$ を探せばよい
- そうすれば $Y^x = g^{xy} = s$ も計算できる
  - $p$ が十分大きいと、$x$ を見つけるのが困難であることが知られている

# 離散対数問題 DLP (Discrete Logarithm Problem)
## 定式化
- $p$, $g$, $X$ が与えられたとき、$X=g^x \bmod{p}$ となる $x$ を求める問題
  - $y=a^x$ のとき $x=\log_a y$ を底 $a$ について $y$ の対数と呼んだ
  - 今回はその整数版なので離散対数という
## DLP を解くコスト
- 2025年現在, 一般数体篩法 GNFS (General Number Field Sieve) が最良の手法
- 計算コストは $L_p[1/3, (64/9)^{1/3}]$
  - $L_p[a, c] := \exp\left((c + o(1))(\log p)^a (\log \log p)^{1-a}\right)$: 準指数時間
  - $f(x)$ が $o(g(n))$ であるとは $\lim_{x \to \infty} f(x)/g(x) = 0$ であること
  - $L_p[1, c] \approx p^c$ （$\log p$ の指数時間）, $L_p[0, c] \approx (\log p)^c$ （$\log p$ の多項式時間）
- 例えば $p = 2^{2048}$ で $2^{116}$, $p=2^{3000}$ で $2^{137}$ 程度
  - 3000bit の素数を使うと128bitセキュリティの安全性があるとみなせる

# DH問題
## DLP が困難だけでOKか?
- $x$, $y$ を求められなくても直接 $s$ を求める方法があるかもしれない
### DHP (Diffie-Hellman Problem)
- $p$, $g$, $X=g^x \bmod{p}$, $Y=g^y \bmod{p}$ が与えられたとき $s=g^{xy} \bmod{p}$ を求めよ
### DLPとDHPの関係
- 先程見たようにDLPが解ければDHPも解ける
  - 問題としてはDHPの方が易しい
  - 2025年現在, DHPを解く最良の手法はDLPを解くこと
  - DHPがDLPより真に易しいか・同じぐらいの難しさかは不明
## 安全性の言い換え
- DHPが困難ならDH鍵共有は安全

# PQC (Post-Quantum Cryptography)
## 量子計算機に対しても安全な暗号技術
- 耐量子計算機暗号
- $\log p$ の多項式時間でDLPを解く量子アルゴリズムが知られている
- 量子計算機が実用化されるとDH鍵共有は安全でなくなる
- 量子計算機に安全な鍵共有方法が必要

## ML-KEM (Module-Lattice Key Encapsulation Mechanism)
- [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final): 2024年NISTで標準化された
- ブラウザ Chrome, Edge, Firefoxなどで利用可能になってきている

- 詳細は後の講義で

# ECDH (Elliptic Curve Diffie-Hellman) 鍵共有
## 楕円曲線を用いた鍵共有
- 現在TLS1.3で標準的に使われている鍵共有手法
- DH鍵共有が3000bitで128bitセキュリティだったのに対して
ECDH鍵共有は256bitで128bitセキュリティを実現する
- 小さい鍵で同じセキュリティを実現できる
## ECDHの量子計算機に対する安全性
- 安全ではない
- $n$ bitのECDHは $O(n^3)$ 程度の多項式時間で解けるアルゴリズムが知られている
