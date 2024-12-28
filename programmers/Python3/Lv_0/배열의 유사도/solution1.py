def solution(s1, s2):
    cnt = 0
    for s in s2:
        if s in s1:
            cnt += 1
    return cnt
