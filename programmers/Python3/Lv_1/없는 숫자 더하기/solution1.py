def solution(numbers):
    result = 0
    for i in range(10):
        if not i in numbers:
            result += i
    return result
