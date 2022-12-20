def solution(k, score):
    result = []
    rank = []
    for sco in score:
        rank.append(sco)
        rank.sort(reverse=True)
        top = rank[:k]
        result.append(top[-1])
    return result
