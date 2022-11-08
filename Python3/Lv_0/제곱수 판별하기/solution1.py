import math

def solution(n):
    root = int(math.sqrt(n))
    if root**2 == n:
        return 1
    else:
        return 2
    