def solution(i, j, k):
    cnt = 0
    for num in range(i, j+1):
        for n in str(num):
            if n == str(k):
                cnt += 1
    return cnt
