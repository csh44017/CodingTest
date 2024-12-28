def solution(s):
    length = len(s)
    center = length//2
    if length%2 == 0:
        return s[center-1] + s[center]
    else:
        return s[center]
    