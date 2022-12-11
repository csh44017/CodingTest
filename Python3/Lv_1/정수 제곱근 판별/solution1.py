import math

def solution(n):
    root_n = int(math.sqrt(n))
    if n == root_n**2:
        return (root_n+1)**2
    else:
        return -1
    