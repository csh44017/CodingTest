import math

def solution(n):
    i = 0
    while True:
        i += 1
        if math.factorial(i) > n:
            return i-1
        