

# 람다(lambda)
```html
lambda 매개변수 : 표현식  
```
함수를 한줄로 간소화 할 수 있는 형식  
```python
sum = (lambda x,y: x + y)(10, 20)
# sum = 30
```
<br>  

# map()
함수와 리스트를 인자로 전달받는다.  
```html
map(함수, 리스트)
```
전달받은 리스트의 원소를 하나씩 꺼내서 함수에 적용 후,  
함수의 결과값을 새로운 리스트에 담는 함수  
```python
square = list(map(lambda x: x**2, range(5)))
# square = [0, 1, 4, 9, 16]
```
<br>python3에서는 list()로 묶어주어야 한다.  
```python
square = map(lambda x: x**2, range(5))
# square = <map object at 0x0000025204A636D0>
```
