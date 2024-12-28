def solution(num_list):
    odd = 0
    even = 0
    result = []
    for num in num_list:
        if num%2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    return [even, odd]
