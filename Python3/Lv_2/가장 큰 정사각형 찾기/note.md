# 점화식  
표의 첫번째 행과 열을 남겨 놓은 뒤,  
(i,j)의 값이 1인 경우마다 2 by 2 사각형 안의 최소값을 반복해서 이용  
<br>  
<blockquote><p> $$\begin{aligned}  
min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1  
\end{aligned}$$</p></blockquote>  
<br>  
모두 1로 이루어져 있지 않다면 0+1로 1 by 1 정사각형의 한변의 길이가 저장됨  
