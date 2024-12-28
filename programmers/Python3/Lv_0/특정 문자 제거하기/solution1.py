def solution(my_string, letter):
    result = ""
    for str in my_string:
        if str != letter:
            result = result + str
    return result
