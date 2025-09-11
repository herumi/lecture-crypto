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

# 数学の準備
## 合同
- 整数 $m(>0)$, $a$, $b$ に対して $a \equiv b \pmod{m}$ とは $(a-b) \bmod{p} = 0$ のときをいう
  - $m$ で割った余りが同じ. このとき $a$ と $b$ は $m$ を法として合同という
  - 注意: 「$a \bmod{m}$」は $a$ を $m$ で割った余り（0以上 $m$ 未満の整数）
## 整数環
- 整数 $m(>0)$ に対して集合 $\mathbb{Z}/m\mathbb{Z} := \{0, 1, 2, \ldots, m-1\}$ とする（$\mathbb{Z}/m$ と略記する）
- 加減算: $a \pm b := (a \pm b) \bmod{p}$. 乗法: $a b := (a b) \bmod{p}$ for $a, b \in \mathbb{Z}/m$
  - 加算と乗算は可換: $a + b = b + a$, $a b = b a$
  - 加法に関する単位元 $0$: $a + 0 = a$, 乗法に関する単位元 $1$: $a \times 1 = a$
  - 結合法則: $(a + b) + c = a + (b + c)$, $(a b) c = a (b c)$
  - 分配法則: $a (b + c) = a b + a c$
- これらを満たすものを可換環という

# 除算の定義
## 思考
- $\mathbb{Z}/m \ni a, b(\neq 0)$ に対して除算 $a/b$ を定義したいが$a/b$ は整数にならない場合がある
- まず逆数 $1/a$ を考える
## 逆数とは
- $ax=1$ となる $x$ が $a$ の逆数
- 整数環でも $ab \equiv 1 \pmod{m}$ となる $b$ があれば $b$ を $a$ の逆数と呼んでよいのでは

- 例えば $m=7$ のとき $3 \times 5 \equiv 1 \pmod{7}$ なので $3$ の逆数 $1/3=5$ とする
- 例えば $m=6$ のとき $3 \times x \not\equiv 1 \pmod{6}$ なので $3$ の逆数は存在しない
  - $3 \times 1 \equiv 3$, $3 \times 2 \equiv 0$, $3 \times 3 \equiv 3$, $3 \times 4 \equiv 0$, $3 \times 5 \equiv 3$
# 有限体
## 素数 $p$ に対する整数環
- $\mathbb{F}_p := \mathbb{Z}/p = \{0, 1, 2, \ldots, p-1\}$
- **定理**: $\forall a \in {\mathbb{F}_p}^*:=\mathbb{F}_p \setminus \{0\}$ に対して $a$ の逆数が存在する
  - つまり $a b \equiv 1 \pmod{p}$ となる $b \in {\mathbb{F}_p}^*$ が存在する
- $\mathbb{F}_p$ は四則演算ができる
  - 逆元の存在: $a \in {\mathbb{F}_p}^*$ に対して $a^{-1}$ が存在して $a a^{-1} = 1$
- このとき $\mathbb{F}_p$ を有限体という

# Euclidの互除法
## 最大公約数 $\gcd(a, b)$ の性質
- $\gcd(a, 0)=a$, $\gcd(a,b)=\gcd(b,a)$.
- $\gcd(a,b)=\gcd(a-b,b)$
  - $c:=\gcd(a,b)$, $c':=\gcd(a-b,b)$ とすると $a = ca'$, $b = cb'$ と書けて $a−b = c(a'−b')$. よって $c$ は $a−b$ と $b$ の公約数となり，$c'$ の最大性から $c \le c'$.
  同様に $a − b = c'x, b = c'y$ と書くと $a = c'(x + y)$. よって $c'$ は $a$ と $b$ の公約数となり, $c$ の最大性から $c' \le c$．よって $c = c'$.
- $b\neq 0$ のとき $\gcd(a,b)=\gcd(a \bmod{b}, b)$.
  - $a$ を $b$ で割った余りになるまで $a-b$ に置き換えることを繰り返す
- $c=\gcd(a,b)$ に対して $b=0$ なら $c=a$ で終了
  - $b>0$ なら $r_0 := a \bmod{b}$ として $c=\gcd(r_0,b)=\gcd(b,r_0)$. $r_0=0$ なら終了
  - $r_0>0$ なら $r_1:=b \bmod{r_0}$ として $c=\gcd(r_1,r_0)$. $r_1=0$ なら終了
  - これを繰り返すといずれ終了し $c$ が求まる

# $\gcd(72, 27)$ の例
## 72と27の長方形を書く
![](images/lec-gcd-sample.png)
- $\gcd(72,27)=\gcd(18,27)=\gcd(27,18)=\gcd(9,18)=\gcd(18,9)=9$

# 拡張Euclidの互除法
## $a$, $b$ に対して $a x + b y = \gcd(a, b)$ となる整数 $x$, $y$ が存在し求められる
- 先程の例で4回で終わったとする
  - $r_0:=a \bmod{b}$: $a = q_0 b + r_0$.
  - $r_1:=b \bmod{r_0}$: $b = q_1 r_0 + r_1$.
  - $r_2:=r_0\bmod{r_1}$: $r_0 = q_2 r_1 + r_2$.
  - $r_3:=r_1\bmod{r_2}=0$: $r_1 = q_3 r_2 + r_3$.
- これを順に代入すると
- $\gcd(a,b)=\gcd(r_0,r_1)=r_2=r_0-q_2 r_1=r_0 - q_2(b-q_1 r_0)$
$=(1+q_1 q_2)r_0 + b(-q_2)=(1+q_1 q_2) (a-b q_0) + b(-q_2)$
$=a(1+q_1 q_2) + b(-q_0 q_1 q_2 - q_2)=a x + by$ となる $(x,y)$ が求まった