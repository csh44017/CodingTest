def solution(num):
    if num == 1: return 0

    result = 0
    while True:
        if num%2 == 0:
            num /= 2
        else:
            num = num*3 + 1
        result += 1

        if num == 1:
            return result
        elif result == 500:
            return -1
        