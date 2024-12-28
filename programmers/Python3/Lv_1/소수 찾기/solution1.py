import math

def solution(n):
    result = 0
    for number in range(2, n+1):
        cnt = 0
        for num in range(2, int(math.sqrt(number))+1):
            if number%num == 0:
                cnt += 1
                break
        if cnt == 0:
            result += 1
    return result
