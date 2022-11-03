def solution(my_string):
    result = ""
    for string in my_string:
        if string not in result:
            result += string
    return result
