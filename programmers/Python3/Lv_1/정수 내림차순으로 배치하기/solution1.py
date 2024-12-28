def solution(n):
    number = [int(string) for string in str(n)]
    number = sorted(number, reverse=True)
    result = ""
    for num in number:
        result += str(num)
    return int(result)
