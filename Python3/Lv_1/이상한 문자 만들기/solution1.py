def solution(s):
    result = ""
    for string in s.split(' '):
        for i in range(len(string)):
            if i%2 == 0:
                result += string[i].upper()
            else:
                result += string[i].lower()
        result += ' '
    return result[:-1]
