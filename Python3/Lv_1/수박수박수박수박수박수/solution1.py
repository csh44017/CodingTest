def solution(n):
    result = ""
    for _ in range(n//2):
        result += "수박"
    if n%2 == 1:
        result += '수'
    return result
