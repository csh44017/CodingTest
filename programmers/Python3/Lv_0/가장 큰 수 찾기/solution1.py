def solution(array):
    result = []
    m = max(array)
    result.append(m)
    result.append(array.index(m))
    return result
