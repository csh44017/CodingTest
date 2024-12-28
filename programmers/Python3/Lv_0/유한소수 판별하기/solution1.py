def solution(a, b):
    for div in range(2, a+1):
        while a%div == 0:
            a = a//div
            if b%div == 0:
                b = b//div
    
    while b%2 == 0:
        b = b//2
    while b%5 == 0:
        b = b//5
    if b == 1:
        return 1
    return 2
