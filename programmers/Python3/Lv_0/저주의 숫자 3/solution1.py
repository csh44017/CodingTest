def solution(n):
    for num in range(1, n+1):
        if (num%3 == 0) or ("3" in str(num)):
            n += 1
            while (n%3 == 0) or ("3" in str(n)):
                n += 1
    return n
