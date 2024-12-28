def solution(my_str, n):
    result = []
    length = len(my_str)//n
    for i in range(length):
        start = n*i
        end = n*(i+1)
        result.append(my_str[start:end])
        if (i+1 == length) and (len(my_str) > length*n):
            result.append(my_str[end:])
    return result
