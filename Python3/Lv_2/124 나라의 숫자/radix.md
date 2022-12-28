# n진법으로 바꾸기  
* divmod()  
파이썬 내장함수로 매개변수로 두 숫자를 입력받아 몫과 나머지를 요소로 가지는 튜플을 반환한다.  
```python  
result = divmod(10, 3)
print(result)
# (3, 1)

q, r = divmod(10, 3)
print(q, r)
# 10, 3
```  

* n진법 변환 함수  
```python  
def radix(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
        
    return rev_base[::-1]
```  
