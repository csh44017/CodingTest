import math

def solution(left, right):
    result = 0
    for num in range(left, right+1):
        cnt = 0
        root = int(math.sqrt(num))
        for i in range(1, root):
            if num%i == 0:
                cnt += 1
        cnt *= 2
        if root**2 == num:
            cnt += 1
            
        if cnt%2 == 0:
            result += num
        else:
            result -= num
    return result
