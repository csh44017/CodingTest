import math
from itertools import combinations

def solution(nums):
    result = 0
    for item in list(combinations(nums, 3)):
        cnt = 0
        num = sum(item)
        for n in range(1, int(math.sqrt(num))+1):
            if num%n == 0:
                cnt += 1
        if cnt == 1:
            result += 1
    return result
