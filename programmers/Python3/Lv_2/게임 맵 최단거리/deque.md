# deque  
파이썬의 deque는 스택과 큐의 기능을 모두 가진 객체이다.  
```python  
from collections import deque
dq = deque('love')

# deque(['l', 'o', 'v', 'e'])
```  
문자열을 넣으면 각 문자를 요소로 하는 리스트 형태의 deque가 생성된다.  

# 스택  
LIFO 구조로 마지막에 해당하는 오른쪽 끝에 있는 항목이 입출력 된다.  
입력 시 : append(), 출력 시 : pop()
```python  
dq.append('m')
dq
# deque(['l', 'o', 'v', 'e', 'm'])
```  
```python
dq.pop()
# 'm'
dq
# deque(['l', 'o', 'v', 'e'])
```  

# 큐  
FIFO 구조로 먼저 입력된 항목이 먼저 출력 된다.
```python  
dq.append('l')
dq
# deque(['l', 'o', 'v', 'e', 'l'])
```  
```python  
dq.leftpop()
# 'l'
dq
# deque(['o', 'v', 'e', 'l'])
```  
