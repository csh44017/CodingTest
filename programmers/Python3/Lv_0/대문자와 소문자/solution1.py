def solution(my_string):
    result = ""
    for string in my_string:
        if string.isupper():
            result += string.lower()
        elif string.islower():
            result += string.upper()
    return result
