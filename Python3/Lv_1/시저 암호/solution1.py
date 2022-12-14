def solution(s, n):
    large = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small = "abcdefghijklmnopqrstuvwxyz"
    length = len(large)
    
    result = ""
    for alpha in s:
        if alpha == ' ':
            result += ' '
        elif alpha.islower():
            idx = small.find(alpha)
            new_idx = (idx+n)%length
            result += small[new_idx]
        else:
            idx = large.find(alpha)
            new_idx = (idx+n)%length
            result += large[new_idx]
    return result
