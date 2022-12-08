def solution(d, budget):
    sorted_d = sorted(d)
    length = len(sorted_d)
    price = 0
    for idx in range(length):
        price += sorted_d[idx]
        if price > budget:
            return idx
        elif price == budget or idx+1 == length:
            return idx+1
        