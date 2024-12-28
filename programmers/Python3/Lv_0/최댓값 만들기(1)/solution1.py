def solution(numbers):
    num1 = max(numbers)
    max_idx = numbers.index(num1)
    numbers.pop(max_idx)
    num2 = max(numbers)
    return num1 * num2
