import math

def solution(n):
    result = 0
    for num in range(2, n+1):
        cnt = 0
        root = int(math.sqrt(num))
        for i in range(1, root+1):
            if num%i == 0:
                cnt = cnt + 1
            if (i == root) and (cnt > 1):
                result += 1
    return result
