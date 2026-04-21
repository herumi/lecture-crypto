# 2×2ユニタリ行列$U$のABC分解

## 記号
- $X:=\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$: NOTゲート
- $R_x(θ):=\begin{pmatrix} \cos(\frac{θ}{2}) & -i\sin(\frac{θ}{2}) \\ -i\sin(\frac{θ}{2}) & \cos(\frac{θ}{2}) \end{pmatrix}$
- $R_y(θ):=\begin{pmatrix} \cos(\frac{θ}{2}) & -\sin(\frac{θ}{2}) \\ \sin(\frac{θ}{2}) & \cos(\frac{θ}{2}) \end{pmatrix}$
- $R_z(θ):=\begin{pmatrix} e^{-iθ/2} & 0 \\ 0 & e^{iθ/2} \end{pmatrix}$

- （ここだけ）$E(θ):=e(iθ)$

## 性質
- $X^2=I$
- $X \begin{pmatrix}a & b \\ c & d\end{pmatrix}=\begin{pmatrix}c & d \\ a & b\end{pmatrix}$: 行列の行を入れ替える
- $\begin{pmatrix}a & b \\ c & d\end{pmatrix} X=\begin{pmatrix}b & a \\ d & c\end{pmatrix}$: 行列の列を入れ替える
- $X R_y(θ) X=X\begin{pmatrix} c & -s \\ s & c \end{pmatrix}X= \begin{pmatrix}s & c\\c & -s\end{pmatrix}X=\begin{pmatrix}c & s \\ -s & c\end{pmatrix}=R_y(-θ)$
- $XR_z(θ)X=\begin{pmatrix}0 & E(iθ/2) \\ E(-iθ/2) & 0\end{pmatrix}X=\begin{pmatrix}E(iθ/2) & 0 \\ 0 & E(-iθ/2)\end{pmatrix}=R_z(-θ)$


## 定理 (Nielsen & Chuang)
- 任意の2×2ユニタリ行列 $U$ に対して $ABC=I$となるユニタリ行列 $A, B, C$ と実数 $α$ が存在し $U = e^{iα} A X B X C$と表せる


### 補題: ZYZ分解
- 任意のユニタリ行列はZYZ分解できる: $U = e^{iα} R_z(β) R_y(γ) R_z(δ)$

両辺を比べて各パラメータを決定する

- $\det(U)=e^{2iα}$なので$α=\arg(U)/2$. よって $U':=U/e^{iα}$とすると$\det(U')=1$

- $U':=\begin{pmatrix}a & b \\ c & d\end{pmatrix}$について$\det(U')=ad-bc=1$ -- (A). ユニタリ性より$|a|^2+|b|^2=|c|^2+|d|^2=1$ -- (B), $a\bar{c}+b\bar{d}=0$ -- (C).
- (C)の両辺に$c$を掛けて$a|c|^2+bc\bar{d}=0$. (A)より$a|c|^2+(ad-1)\bar{d}=a-\bar{d}=0$. よって$d=\bar{a}$.
- 再度(C)より$a(\bar{c}+b)=0$. $a≠0$なら$c=-\bar{b}$. $a=0$なら$d=0$で$|b|=|c|=1$かつ$-bc=1$より$c=-\bar{b}$.
- よって$U':=\begin{pmatrix}a & b \\ -\bar{b} & \bar{a}\end{pmatrix}$.

$a=E(s)\cos(γ/2)$, $b=E(t)\sin(γ/2)$とする

$W:=R_z(β)R_y(γ)R_z(δ)$ とすると

$W=\begin{pmatrix} E(-i(β+δ)/2) \cos(γ/2) & -E(-i(β-δ)/2) \sin(γ/2) \\ E(i(β-δ)/2) \sin(γ/2) & E(i(β+δ)/2) \cos(γ/2) \end{pmatrix}$ は $U'$と同じ形をしているので

$U'=W$とすると$s=-(β+δ)/2$, $t=(β-δ)/2$. よって$β=-\arg(a)+\arg(b)$, $δ=-\arg(a)-\arg(b)$.

つまり$α, β, γ, δ$を上記のように取ると$U'$をZYZ分解できる. □

### 定理の証明
$A:= R_z(β) R_y(γ/2)$, $B:= R_y(-γ/2) R_z(-(δ+β)/2)$, $C:= R_z((δ-β)/2)$とすると定理の条件を満たす.

- $ABC = R_z(β)R_y(γ/2)R_y(-γ/2)R_z(-(δ+β)/2)R_z((δ-β)/2)=R_z(β) R_z(-β) = I$.
- $X B X = X R_y(-γ/2) (X X) R_z(-(δ+β)/2) X = R_y(γ/2) R_z((δ+β)/2)$.
- $AXBXC = R_z(β) R_y(γ/2) R_y(γ/2) R_z((δ+β)/2)R_z((δ-β)/2)= R_z(β) R_y(γ) R_z(δ)=U'$. □
