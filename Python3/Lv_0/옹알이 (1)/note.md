<h1> 모든 조합 구하기</h1>  
조건에 맞는 모든 순열 조합을 tuple에 담음<br><br>  

* 순서를 고려한 경우의 조합  
```python
from itertools import permutations

result = []
for i in list(permutations(items, 2)):
    result.append(i)
# result = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)]
```

* 순서를 고려하지 않은 경우의 조합  
```python
from itertools import combinations

result = []
for i in list(combinations(items, 2)):
    result.append(i)
# result = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
```
