def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    
    lend = 0
    for id in new_lost:
        if id-1 in new_reserve:
            lend += 1
            new_reserve.remove(id-1)
        elif id+1 in new_reserve:
            lend += 1
            new_reserve.remove(id+1)
    return n - len(new_lost) + lend
