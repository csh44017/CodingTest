def solution(s):
    result = []
    for i in range(len(s)):
        idx = s[:i].rfind(s[i])
        if idx != -1:
            idx = i - idx
        result.append(idx)
    return result
