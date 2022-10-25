def solution(my_string, n):
    result = ""
    for str in my_string:
        for _ in range(n):
            result = result + str
    return result
