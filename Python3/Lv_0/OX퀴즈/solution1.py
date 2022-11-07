def solution(quiz):
    result = []
    for q in quiz:
        calc = q.split("=")
        if eval(calc[0]) == int(calc[1]):
            result.append("O")
        else:
            result.append("X")
    return result
