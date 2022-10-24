def solution(numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum/len(numbers)
