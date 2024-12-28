def solution(X, Y):
    common = []
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for n in num:
        cnt_x = str(X).count(n)
        cnt_y = str(Y).count(n)
        for _ in range(min(cnt_x, cnt_y)):
            common.append(int(n))
    
    if len(common) == 0:
        return "-1"
    elif len(common) == common.count(0):
        return "0"
    else:
        result = ""
        common.sort(reverse=True)
        for c in common:
            result += str(c)
        return result
    