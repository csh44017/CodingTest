def solution(emergency):
    s = sorted(emergency)
    s.reverse()
    result = []
    for e in emergency:
        result.append(s.index(e)+1)
    return result
