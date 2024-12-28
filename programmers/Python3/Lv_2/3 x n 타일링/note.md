# 3 x n 타일링 점화식  
짝수인 경우에만 바닥을 가득 채울 수 있음  
<br>
<blockquote><p> $$\begin{aligned}  
  f(n) &= f(n-2)\cdot3 + f(n-4)\cdot2 + … + f(2)\cdot2 + 2  \\
  &= f(n-2)\cdot3 + (f(n-4) + … + f(2))\cdot2 + 2  
\end{aligned}$$</p></blockquote>  
