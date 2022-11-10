def solution(my_string):
    result = 0
    num_str = ""
    for string in my_string:
        if string.isalpha():
            num_str += " "
        else:
            num_str += string
    for num in num_str.split():
        result += int(num)
    return result
