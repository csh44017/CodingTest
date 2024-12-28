def solution(score):
    average = list(map(lambda x: (x[0]+x[1]) / 2, score))
    average.sort(reverse=True)
    
    result = []
    for sco in score:
        avg = (sco[0]+sco[1]) / 2
        result.append(average.index(avg)+1)
    return result
