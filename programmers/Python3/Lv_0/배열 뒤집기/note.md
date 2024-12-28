# reverse()
리스트에 들어있는 요소들의 순서를 거꾸로 뒤집는다. (반환 값 X)  
```python  
arr = [5, 10, 15, 20, 25]
arr.reverse()
print(arr)
# [25, 20, 15, 10, 5]
```  
<br>  

# reversed()
리스트에 들어있는 요소들의 순서를 거꾸로 뒤집는다. (반환 값 O)
```python  
arr = [5, 10, 15, 20, 25]
print(reversed(arr))
# <list_reverseiterator object at 0x0000022F96FE6A40>
```
```python  
arr = [5, 10, 15, 20, 25]
print(list(reversed(arr)))
# [25, 20, 15, 10, 5]
```  
```python  
arr = [5, 10, 15, 20, 25]
for i in reversed(arr):
    print(i)
# 25
# 20
# 15
# 10
# 5
```  
