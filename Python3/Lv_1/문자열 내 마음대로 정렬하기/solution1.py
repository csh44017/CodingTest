def solution(strings, n):
    dict = {}
    for alpha in "abcdefghijklmnopqrstuvwxyz":
        dict[alpha] = []
    
    for string in strings:
        dict[string[n]].append(string)
    
    result = []
    for alpha in dict:
        if dict[alpha]:
            dict[alpha].sort()
            for s in dict[alpha]:
                result.append(s)
    return result
