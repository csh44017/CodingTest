# 동적 계획법(Dynamic Programming)  
최적화 이론의 한 기술로, 특정 범위까지의 값을 구하기 위해서 그것과 다른 범위까지의 값을 이용하여 효율적으로 값을 구하는 알고리즘 설계 기법  
분할 정복 알고리즘과 접근 방식이 비슷하다.  
```python  
mem = [-1 for i in range(60001)]

def dp(n):
    if mem[n] != -1: return mem[n]
    if n == 0: return 1
    if n == 1: return 1
    mem[n] = (dp(n-1) + dp(n-2)) % 1000000007
    return mem[n]
```  

* 메모이제이션(memoization)  
컴퓨터 프로그램이 동일한 계산을 반복해야 할 때, 이전에 계산한 값을 메모리에 저장함으로써 동일한 계산의 반복 수행을 제거하여 프로그램의 실행 속도를 빠르게 하는 기술로 
동적 계획법의 핵심이 된다.<br><br>  
  - 점화식  
  수열에서 이웃하는 두개의 항 사이에 성립하는 관계를 나타낸 관계식  

  <blockquote><p> $$\begin{aligned}  
    a_{n+1} = f(a_n)  
  \end{aligned}$$</p></blockquote>  

  - 피보나치 수열  
  첫째 및 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열  
  <blockquote><p> $$\begin{aligned}  
    &F_1 = F_2 = 1 \\  
    &F_n = F_{n-1}+F_{n-2} &(n = 3, 4, 5, ...)  
  \end{aligned}$$</p></blockquote>  
```python  
DP(n) = DP(n-1) + DP(n-2)
```  
  
