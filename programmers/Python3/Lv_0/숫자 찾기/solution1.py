def solution(num, k):
    str_num = str(num)
    result = str_num.find(str(k))
    if result != -1:
        result += 1
    return result
