def solution(babbling):
    result = 0
    items = ["aya", "ye", "woo", "ma"]
    no_items = ["ayaaya", "yeye", "woowoo", "mama"]

    for bab in babbling:
        if (bab.count(no_items[0]) != 0) or (bab.count(no_items[1]) != 0) or (bab.count(no_items[2]) != 0) or (bab.count(no_items[3]) != 0):
            continue
        cnt = 0
        for item in items:
            cnt += bab.count(item)*len(item)
        if cnt == len(bab):
            result += 1
    return result
