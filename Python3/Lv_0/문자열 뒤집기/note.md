#slice  
slice의 항목은 다음과 같다.
```html  
[start:stop:step]
```  
전체 문자열을 -1 스텝으로 슬라이스하면 반대 방향으로 리스트의 데이터를 자를 수 있다.
```python  
string = "Hello"
reversed_string = string[::-1]
print(reversed_string)
# "olleH"
```  
<br>  

#reversed()
반대방향의 iterator를 리턴한다.
<br>  

join() 함수를 통해 리턴된 iterator의 데이터를 하나로 합칠 수 있다.
```python  
string = "Hello"
reversed_string = "".join(reversed(string))
print(reversed_string)
# "olleH"
```
