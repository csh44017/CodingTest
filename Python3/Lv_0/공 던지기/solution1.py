def solution(numbers, k):
    length = len(numbers)
    index = (k-1)*2
    result = numbers
    while length < (index+1):
        result = result + numbers
        if len(result) >= (index+1):
            break
    return result[index]
    