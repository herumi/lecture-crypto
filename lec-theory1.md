---
marp: true
html: true
title: slides
theme: default
paginate: true
size: 16:9
style: |
  section {
    justify-content: flex-start;
    margin: 0px;
    background-color: white;
    padding: 0px;
    background: linear-gradient(180deg,#E7FFE7 10%, #008080 10%,#008080 10.5%, white 10.5%, white 100%);
    display: flex;
    font-family: Noto Sans JP;
  }
  code {
    font-family: 'BIZ UDGothic', monospace;
  }
  pre {
    font-family: inherit;
  }
  pre code {
    font-family: 'BIZ UDGothic', monospace;
  }
  section h1 {
    margin: 0px;
    padding-left: 10px;
    padding-top: 5px;
    padding-bottom: 3px;
    background-size: 15%;
    background-repeat: no-repeat;
    background-position: right 5px top 5px;
  }
  section.title {
    font-size: 200%;
    padding: 40px;
    background: linear-gradient(180deg,#E7FFE7 49%, #008080 49%,#008080 50%, white 50%, white 100%);
    text-align: center;
    justify-content: center;
  }
  section h2 {
    padding-left: 10px;
    padding-top: 0px;
    padding-bottom: 0px;
  }
  section h3 {
    padding-left: 30px;
    padding-top: 0px;
    padding-bottom: 0px;
  }
  section ul {
    margin: 0px;
  }
  section::after {
   font-size: 70%;
   content: attr(data-marpit-pagination) " / " attr(data-marpit-pagination-total);
  }
  table {
    margin-left: auto;
    margin-right: auto;
    table-layout: fixed;
    width: auto;
    display:table;
  }
  thead th {text-align: center !important;}
  thead tr {background: #eaeaea;}
  tbody tr:nth-child(2n+1) {text-align: center !important;background: #fff;}
  tbody tr:nth-child(2n) {text-align: center !important;background: #eeeeee;}
  section .emp { color: red; }
  section pre {
    margin: 0px;
  }
  em {
    color: red;
    font-style: normal;
  }
  img {
    display: inline;
    vertical-align: top;
  }
---
<!--
headingDivider: 1
-->
<!--
_class: title
-->
# 暗号理論の準備
<br>
光成滋生
<br>

# 数学的な定義
## 記法
- $\exists a$～: 存在記号: 「～となる $a$ が存在して...」
- $\forall a$～: 全称記号: 「～となる全ての $a$ に対して...」
## 定義と読み方
- $f(n)=O(g(n))$ とは $\exists c>0$, $\exists N>0$ s.t. $\forall n \ge N$, $|f(n)/g(n)| \le c$.
  - ある $c>0$ が存在し、$n \ge N$ となる全ての $n$ に対して $|f(n)/g(n)|\le c$ が成り立つような $N>0$ が存在する（s.t. = such thatの略）
## 意味するところ
- まず定数 $c$ が固定して決まり、その $c$ に対して次の条件を満たす定数 $N$ を決められる
  - $n \ge N$ ならば $|f(n)/g(n)| \le c$ である
- $n<N$ のときは例外があるかもしれないけど十分大きく ($n\ge N$) とれば $c$ 以下にできる

# 例
## $f(n)=3n^2 + 5n + 4=O(n^2)$
### 直感的には
- $f(n)/n^2=3+5/n+4/n^2→3 (n→∞)$ だから $f(n)=O(n^2)$
### 定義にしたがって確認すると
- $c=4$ とする（3より大きな値を適当に決めた）
- $5/n+4/n^2 < 1$ なる $n$ を考える
- $n \ge 10$ なら $5/n+4/n^2 \le 5/10+4/100=1/2+1/25<1$
- よって $N=10$ とすると $n \ge N$ なら $f(n)/n^2 \le 3 + 1 = c$ である（QED）
  - もちろんもっと厳密に $c$ や $N$ を求めてもよいが存在を示せばよいので大雑把でもよい

# 問題
## 簡単
1. $\sin(x)=O(1)$ を示せ.
## 中級
2. どんな $k>0$ についても $e^n=O(n^k)$ とはならないことを示せ
- $e^n=\sum_{i=0}^{\infty} \frac{n^i}{i!}$ であることを利用してよい

# 無視できる関数
## 十分小さいことを表す
- $f:\mathbb{N} \to \mathbb{R}_{\ge 0}$ が無視できる (negligible) とは $\forall c > 0$, $\exists N \in \mathbb{N}$ s.t. $\forall n > N$, $f(n)<n^{-c}$.
  - $c>0$ をどんなに大きくとっても、それに対応して十分大きく $N$ を選べば、
  それより大きい $n>N$ について $f(n) < n^{-c}$ とできる
- $f(n)$ はどんな多項式の逆数よりも速く小さくなる
- このとき $f(n) < \mathtt{negl}(n)$ と書く（$f(n)<ε(n)$ と書くこともある）

## 例
- $e^{-n}=\mathtt{negl}(n)$
- $e^n$ はどんな多項式よりも速く大きくなるのでその逆数はとても速く小さくなる
  - 任意の $c>0$ に対して $k=\mathtt{ceil}{(c)}+1$ とすれば $e^n > n^k/k!$.
  - $N=k!$ とすれば $n>N$ なら $e^{-n} < n^{-k}k!=n^{-k+1}(k!/n)<n^{-(k-1)}\le n^{-c}$.

# 確率的多項式時間アルゴリズム
## 決定的 (deterministic) 多項式時間 PT (Polynomial Time) アルゴリズム
- $n$ bitの入力 $x \in \Set{0,1}^n$ に対して常に同じ値 $f(x)$ を返す
- 実行時間が $n$ に関する多項式時間
## 確率的 (probabilistic) 多項式時間 PPT アルゴリズム
- $n$ bitの入力 $x$ に対して乱数 $r$ を取得し $f(x,r)$ を返す（$r$ によって値が変わり得る）
- 実行時間が $n$ に関する多項式時間
## $n$ ビットの整数 $x$ について
- $x$ が素数であるかどうかを判定する $n$ についての決定的PTアルゴリズムがある（非効率）
- $x$ が合成数か、判定不能かを返す効率のよいPPTアルゴリズムが存在する
  - 繰り返し適用してずっと判定不能なら多分素数
  - 十分小さい確率を無視して $x$ が素数であるとみなせる

# 疑似乱数
## 一様ランダム
- 集合 $S$ からどの要素も同じ確率で取り出すとき $x \underset{U}{\leftarrow} S$ と書く
## 理想の乱数と疑似乱数の違いは何か?
- 小さい値 (seed) から*決定的*アルゴリズムで長い疑似乱数列を生成したとき、
それが本物の乱数と見分けがつかない
- 見分ける人の能力を考える
  - 攻撃者も通常の計算機を使うと考えてPPTアルゴリズムを実行すると仮定する
- 「見分けがつかない」を無視できる関数で表現する

# 疑似乱数の定義
### $G:\Set{0,1}^n \to \Set{0,1}^{l(n)}$ がPRGであるとは次を満たすもの
- $l(n) > n$ である多項式
- $\forall {\cal A}(x) \in \Set{0,1}$: PPT多項式について
$\left| \Pr \left[{\cal A}(r)=1 \mid r \underset{U}{\leftarrow} \Set{0,1}^{l(n)} \right] - \Pr \left[{\cal A}(G(s))=1 \mid s \underset{U}{\leftarrow} \Set{0,1}^{n} \right]\right| < \texttt{negl}(n)$
### 意味
- ${\cal A}(x)$ は $x$ が乱数と判定すれば1, そうでなければ0を返す攻撃者（判定者）
  - $l(n)$ bitの真の乱数 $r$ を選ぶ
  - $n$ bitの真の乱数 $s$ から $l(n)$($>n$) bitの疑似乱数 $G(s)$ を作る
  - 両者をそれぞれ ${\cal A}$ に渡して乱数と判定する確率の差が無視できる
- どんな判定者も区別できないなら、その疑似乱数は真の乱数とみなしてよいだろう
  - 計算量的識別不可能な疑似乱数