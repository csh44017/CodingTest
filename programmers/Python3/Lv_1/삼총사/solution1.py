from itertools import combinations

def solution(number):
    cnt = 0
    for num in list(combinations(number, 3)):
        if num[0] + num[1] + num[2] == 0:
            cnt += 1
    return cnt
