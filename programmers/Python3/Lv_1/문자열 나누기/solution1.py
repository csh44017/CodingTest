def solution(s):
    cnt_eq, cnt_diff = 0, 0
    result = 0
    for i in range(len(s)):
        if cnt_eq == 0 and cnt_diff == 0:
            x = s[i]
            
        if x == s[i]: cnt_eq += 1
        else: cnt_diff += 1
            
        if cnt_eq == cnt_diff:
            result += 1
            cnt_eq = cnt_diff = 0
        else:
            if i == len(s)-1:
                result += 1
    return result
