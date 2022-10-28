def solution(balls, share):
    result = 1
    for mul in range(balls-share+1, balls+1):
        result = result * mul
    for div in range(2, share+1):
        result = result // div
    return result
