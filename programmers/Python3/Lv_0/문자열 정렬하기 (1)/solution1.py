def solution(my_string):
    result = []
    num = "0123456789"
    for n in num:
        for string in my_string:
            if string == n:
                result.append(int(n))
    return result
