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
# 公開鍵暗号3
<br>
光成滋生
<br>
last update: 2025/10

# 目次
## 用語一覧
- 公開鍵暗号

# 公開鍵暗号
## PKEとPKC
<!-- _class: image-right -->
![w:500px](images/lec-pkc-pke.drawio.svg)
- 「公開鍵暗号」には二種類の意味がある
- PKE (Public Key Encryption)
  - 公開鍵で暗号化して秘密鍵で復号する暗号方式
  公開鍵暗号化・公開鍵暗号方式とも
- PKC (Public Key Cryptography)
  - 公開情報と秘密情報を組み合わせた暗号技術全般
  - 鍵共有, 署名, 暗号化などを含む
    - 今まで紹介してきたのは鍵共有と署名
## 機能と構成要素
- 準同型暗号: 暗号文のまま演算ができる暗号（機能面による命名）
- 楕円曲線暗号: 楕円曲線を使った暗号技術全般（構成要素による命名）
  - 他にペアリング暗号・格子暗号など

# PKEの定義
## PPTアルゴリズムの組 $Π:(Keygen, Enc, Dec)$ がPKEであるとは
- KeyGen: 鍵生成
  - $KeyGen(1^λ) \to (pk, sk)$: $λ$: セキュリティパラメータ, $pk$: 公開鍵, $sk$: 秘密鍵
  - 平文空間 ${\cal M}$ も決まる
- Enc: 平文 $m \in {\cal M}$ の暗号化
  - $Enc(pk, m) \to c$
- Dec: 暗号文 $c$ の復号（Decは決定的アルゴリズム）
  - $Dec(sk, c) \to m$
- 正当性: 任意の $m \in {\cal M}$ に対して $Dec(sk, Enc(pk, m)) = m$

# PKEとIND-CPA安全
## IND-CPA安全 （再掲）
- 自分で選んだ平文 $m_1$, $m_2$ のどちらかの暗号文 $c$ をもらってもどちらの平文か当てられない
## 平文当てゲーム $\texttt{Exp}(λ)$: 実験 (experiment)
1. 挑戦者 C (Challenger): $s =KeyGen(1^λ)$
1. 敵対者 A (Adversary): $m_1, m_2 \in {\cal M}$ を選ぶ
1. C: $b \in\Set{0,1}$ を選び $c=Enc(s,m_b)$ を A に送る
1. A: $c$ から $b' \in \Set{0,1}$ を推測して $b=b'$ ならAの勝ち
<img src="images/lec-cpa-game.drawio.svg" width="400px" style="float:right;margin-top:-300px;margin-right:10px">
- IND-CPA安全とは $Adv_{Exp}(λ):=\left| \Pr \left[Exp(λ)=1\right] - \frac{1}{2} \right|<\texttt{negl}(λ)$ for $\forall$ PPT Algo $Exp$
## 共通鍵暗号とPKEの違い
- PKEでは任意の $m$ の暗号文を自分で作れる $c=Enc(pk,m)$ のでIND-CPA安全は必須条件

# 安全ではないPKEの例
## RSA関数をそのまま使うRSA暗号（RSA$_0$ とここでは表記）
- $KeyGen(1^λ)$: RSA関数の設定
  - 素数 $p, q$ と $(e,d)$ を $e d \equiv 1 \pmod{(p-1)(q-1)}$ となるように選び $n:=p q$ とする
  - $pk:=(n,e)$, $sk:=(p,q,d)$, ${\cal M}:=[0,n-1]$
- $Enc(pk, m)$: $m \in {\cal M}$ に対して $c = m^e \bmod n$
- $Dec(sk, c)$: $m = c^d \bmod n$

## RSA$_0$ はIND-CPA安全ではない
- $c=Enc(pk,m_b)$ をもらったら $c_i:=Enc(pk,m_i)$ ($i=1,2$) を計算して
$c=c_1$ か $c=c_2$ かを調べればどちらの平文を暗号化したのか当てられる
- より一般にPKEの暗号化 $Enc$ が決定的アルゴリズムならばIND-CPA安全ではない
  - IND-CPA安全なPKEの暗号化はPPTアルゴリズムでなければならない
  - 便宜上, 暗号化に使った乱数 $r$ を明示的に $Enc(s,m;r)$ と書くことがある

# 楕円ElGamal暗号
## 定義
- KeyGen: 楕円曲線を用いて位数 $r$ の巡回群 $G=⟨P⟩=\Set{0,P,2 P, \dots, (r-1)P}$ を選ぶ
  - $s \underset{U}\leftarrow  [1,r-1]$: 秘密鍵, $Q = s P$: 公開鍵, ${\cal M} = G$
- Enc: $M \in G$ に対して $k \underset{U}\leftarrow [1,r-1]$ を選び $c:=Enc(Q,M;k) := (k P, M + k Q)$
- Dec: $c=(A,B)$ に対して $Dec(s, c)=B - s A$
## 正当性
- $Dec(s,Enc(Q,M;k))=(M+k Q)-s(k P) = M + k s P - s k P = M$

# 楕円ElGamal暗号はIND-CPA安全
## 安全性仮定の根拠は?
- IND-CPAのゲームで敵対者 A は $c=Enc(Q,M_b;k)$ を受け取る
自分で $M_i$ ($i=1,2$) の暗号文 $c_i:=Enc(Q,M_i;k_i)$ を作り比較する
- $c$ と $c_i$ の成分ごとに引き算して $c - c_i = ((k-k_i) P, (M_b-M_i) + (k-k_i) Q)$ を得る
- $b=i$ となる方は $(k-k_i)P$, $(k-k_i)Q=(k-k_i) sP$ である
## DDH問題 (Decisional DH problem)
- $G=⟨P⟩ \ni P, a P, b P, c P$ が与えられたとき $c = a b$ かを判定する問題
- もし DH問題が解けるなら $P, aP, b P$ から $a b P$ を求めて $c P$ と比較すればDDHは解ける
- DDH問題が難しいという仮定をDDH仮定という
## 楕円ElGamal暗号はDDH仮定の元でIND-CPA安全
- $P$, $s P$, $(k-k_i) P$ が分かっているので残りが $(k-k_i)s P$ かどうか判定できない

# IND-CCA(1/2)安全（再掲）
<!-- _class: image-right -->
![w:500px](images/lec-cca2.png)
## 選択暗号文攻撃CCA
- 攻撃者 $\cal A$ は好きな暗号文 $c_i (\neq c)$ を選び
対応する平文 $m'=Dec(c_i)$ を得られる状況
  - その時 $Dec(c)$ が $m_i$ のどちらか当てられるか?
- CCA1: $c$ を受け取る前のみクエリ可能
- CCA2: $c$ を受け取った後もクエリ可能
- 当てられないならIND-CCA(1/2)安全
## ElGamal暗号はIND-CCA2安全ではない
- $\cal A$ は $c=Enc(Q,M)=(A,B):=(k P, M + k Q)$ から $c'=(A+P,B+Q)$ を作る
- $c'\neq c$ なので挑戦者に復号してもらう: $Dec(c')=(B+Q)-s(A+P)=B-s A = M$
- $M$ が分かるので当てられる
- ElGamal暗号がDDH仮定の元でIND-CCA1安全かそうでないかは未解決
