def solution(s):
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for alpha in alphabet:
        if s.count(alpha) == 1:
            result += alpha
    return result
