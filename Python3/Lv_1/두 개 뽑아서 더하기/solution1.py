from itertools import permutations

def solution(numbers):
    sum_list = []
    for number in list(permutations(numbers, 2)):
        sum_list.append(number[0]+number[1])
    sum_list = list(set(sum_list))
    sum_list.sort()
    return sum_list
