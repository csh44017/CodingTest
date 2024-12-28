# list to np.array  
- np.array()  
```python  
import numpy as np

li = [1, 2, 3, 4]
arr = np.array(li)
# array([1, 2, 3, 4])
```  

# np.array to list  
**list(arr)** 를 사용하면 'object of type ndarray is not json serializable' 오류가 발생할 수 있다.
- tolist()  
```python  
import numpy as np

arr = np.arange(10)
li = arr.tolist()
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

# reshape()  
numpy.ndarray의 차원과 모양을 바꿔준다.  
<br>데이터의 개수와 형태의 크기가 같아야 사용할 수 있다.  
list와 같은 ndarray 이외의 자료형은 reshape()를 사용하면 오류가 발생한다.  
```python  
import numpy as np

li = [1, 2, 3, 4, 5, 6, 7, 8]
arr = np.array(li).reshape((2,4))
# array([1, 2, 3, 4],
#       [5, 6, 7, 8]])
```  
reshape(n, -1) 은 n의 크기에 맞게 형태를 변형시킨다.  
```python  
arr = np.arange(10)
arr.reshape(2, -1)
# array([[0, 1, 2, 3, 4],
#        [5, 6, 7, 8, 9]])
```  
