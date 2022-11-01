def solution(box, n):
    result = []
    for i in box:
        result.append(i//n)
    return result[0] * result[1] * result[2]
