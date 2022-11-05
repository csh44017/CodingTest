def solution(order):
    number = str(order)
    cnt = 0
    for num in number:
        if (num == '3') or (num == '6') or (num == '9'):
            cnt += 1
    return cnt
