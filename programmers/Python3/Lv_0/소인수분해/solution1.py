def solution(n):
    num = 1
    result = [num]
    for i in range(2, n+1):
        while n%i == 0:
            n = n//i
            num = i
        if result[-1] != num:
            result.append(num)
    return result[1:]
