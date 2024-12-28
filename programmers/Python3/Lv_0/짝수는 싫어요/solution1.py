def solution(n):
    odd = []
    for num in range(n+1):
        if (num%2) == 1:
            odd.append(num)
    return odd
