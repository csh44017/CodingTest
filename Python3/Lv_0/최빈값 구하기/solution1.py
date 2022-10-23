from collections import Counter


def solution(array):
    cnt = Counter(array)
    order = cnt.most_common()
    mode = order[0][0]
    maximum = order[0][1]
    
    if len(order) > 1:
        if order[1][1] == maximum:
            return -1
    return mode
