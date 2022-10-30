# list to np.array  
- np.array()  
```python  
import numpy as np

li = [1, 2, 3, 4]
arr = np.array(li)
# array([1, 2, 3, 4])
```  

# np.array to list  
- tolist()  
```python  
import numpy as np

arr = np.arange(10)
li = arr.tolist()
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

# reshape()  
list와 같은 ndarray 이외의 자료형은 reshape()를 사용하면 오류가 발생한다.
```python  
import numpy as np

li = [1, 2, 3, 4, 5, 6, 7, 8]
arr = np.array(li).reshape((2,4))
# array([1, 2, 3, 4],
#       [5, 6, 7, 8]])
```
