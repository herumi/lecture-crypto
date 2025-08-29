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
# 暗号理論の初歩
<br>
光成滋生
<br>

# 計算量
## アルゴリズムの善し悪し
- 同じ結果を得るならより速いアルゴリズムがよい
- 少ないメモリ・少ない時間
- 入力パラメータの大きさ $n$ について $n$ が大きくなったときの振る舞いをみる
## O記法（オー）
- 関数 $f(n)$ が $n$ の増加に伴いどのように増加するかを表す記法
## 例
- $f(n)=O(1)$: 定数時間: $f(n)$ は $n$ がどんなに増えてもある定数以下である
- $f(n)=O(n^d)$: 多項式時間: $f(n)$ は $n$ が大きいとき高々 $n^d$ の定数倍の大きさ
- $f(n)=O(\log(n))$: 対数時間: $f(n)$ は $n$ が大きいとき高々 $\log(n)$ の定数倍の大きさ
- $f(n)=O(e^n)$: 指数時間: $f(n)$ は $n$ が大きいとき高々 $e^n$ の定数倍の大きさ

# 計算量のグラフ
## 比較
![bg right:40% w:500px](images/lec-compare-graph.png)
- 定数時間 $<$ 対数時間 $<$ 多項式時間 $<$ 指数時間
- $2^x$ は指数時間, $x^{100}$ は多項式時間
  - $x=10$ のときは $2^x \ll x^{100}$ だけれども
## 大雑把な目安
- 現在のコンピュータでは $2^{128}$ 個の計算は無理
- $2^{80}$ ぐらいはできる


# 数学的な定義
## 記法
- $\exists a$～: 存在記号: 「～となる $a$ が存在して...」
- $\forall a$～: 全称記号: 「～となる全ての $a$ に対して...」
## 定義と読み方
- $f(n)=O(g(n))$ とは $\exists c>0$, $\exists N>0$, $\forall n \ge N$, $|f(n)/g(n)| \le c$.
  - ある $c>0$ が存在し、ある $N>0$ が存在し、
$n \ge N$ となる全ての $n$ に対して $|f(n)/g(n)|\le c$ が成り立つ
## 意味するところ
- まず定数 $c$ が固定して決まり、その $c$ に対して定数 $N$ が決まる
  - そのとき $n \ge N$ ならば必ず $|f(n)/g(n)| \le c$ である
- $n<N$ のときは例外があるかもしれないけど十分大きく($n\ge N$)なれば $c$ で抑えられる

# 例
## $f(n)=3n^2 + 5n + 4=O(n^2)$
### 直感的には
- $f(n)/n^2=3+5/n+4/n^2→3 (n→∞)$ だから $f(n)=O(n^2)$
### 定義にしたがって確認すると
- $c=4$ とする（3より大きな値を適当に決めた）
- $5/n+4/n^2 < 1$ なる $n$ を考える
- $n>10$ なら $5/10+4/100=1/2+1/25<1$
- よって $N=10$ とすると $n \ge N$ なら $f(n)/n^2 \le 3 + 1 = c$ である（QED）
  - もちろんもっと厳密に $c$ や $N$ を求めてもよいが存在を示せばよいので大雑把でもよい
1. $\sin(x)=O(1)$ を示せ.
2. どんな $k>0$ についても $e^n=O(n^k)$ とはならないことを示せ