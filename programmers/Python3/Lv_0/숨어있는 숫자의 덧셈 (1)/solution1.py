def solution(my_string):
    result = 0
    num = "0123456789"
    for n in num:
        for string in my_string:
            if string == n:
                result += int(n)
    return result
