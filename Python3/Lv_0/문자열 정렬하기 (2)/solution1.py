def solution(my_string):
    result = ""
    alpha = list(my_string.lower())
    alpha.sort()
    for a in alpha:
        result += a
    return result
