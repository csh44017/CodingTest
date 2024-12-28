def solution(cipher, code):
    result = ""
    length = len(cipher)//code
    for mult in range(1, length+1):
        result += cipher[code*mult - 1]
    return result
