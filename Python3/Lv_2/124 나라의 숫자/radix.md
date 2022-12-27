# n진법으로 바꾸기  

aa  

```python  
def radix(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
        
    return rev_base[::-1]
```  
