# collections.Counter  
collection 모듈의 Counter 클래스는 리스트 또는 튜플에서 각 데이터가 등장한 횟수를 딕셔너리 형식으로 반환한다.  
이를 이용하여 최빈값을 구할 수 있다.  
```html  
모드(mode)는 통계학 용어로 가장 많이 관측되는 수, 즉 주어진 값 중에서 가장 자주 나오는 값이다.
(최빈값은 산술 평균과 달리 유일한 값이 아닐 수도 있다.)
```  
```python  
from  collections import Counter

animals = ['dog', 'cat', 'dog', 'bear', 'bear', 'bear']
cnt = Counter(animals)
# cnt = Counter({'bear': 3, 'dog': 2, 'cat': 1})
```  
<br>  

# collections.Counter.most_common  
Counter 클래스의 most_common() 메쏘드는 등장한 횟수를 내림차순으로 정리하여 리스트로 반환한다.  
(등장한 횟수가 동일한 대상이 여러개라면 임의의 순서로 정렬)  
<br>리스트에는 '**가장 많이 등장한 대상**'과 '**횟수**'를 요소로 하는 튜플이 들어있다.  
```python  
mode = cnt.most_common()
# mode = [('bear', 3), ('dog', 2), ('cat', 1)]
```  
상위 n개의 결과만 반환하고 싶다면 n을 인자로 넣어주면 된다.  
```python  
mode = cnt.most_common(2)
# mode = [('bear', 3), ('dog', 2)]
```
최빈값 반환
```python  
return mode[0][0]
# mode[0][0] = 'bear'
# mode[0][1] = 3
```
