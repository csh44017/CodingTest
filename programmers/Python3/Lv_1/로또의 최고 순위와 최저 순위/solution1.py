def solution(lottos, win_nums):
    num_list = []
    for i in range(1, 46):
        num_list.append(i)

    win_cnt = 0
    error_cnt = 0
    for lotto in lottos:
        if lotto in win_nums:
            win_cnt += 1
        elif lotto == 0:
            error_cnt += 1
    
    high = 7 - (win_cnt + error_cnt)
    low = 7 - win_cnt
    if high >= 6:
        high = 6
    if low >= 6:
        low = 6
    return [high, low]
