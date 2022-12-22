def solution(t, p):
    result = 0
    len_t, len_p = len(t), len(p)
    for i in range(len_t-len_p+1):
        tmp = t[i:i+len_p]
        if int(tmp) <= int(p):
            result += 1
    return result
