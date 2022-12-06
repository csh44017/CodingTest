import re

def solution(dartResult):
    numbers = re.findall(r'\d+', dartResult)
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for n in num:
        dartResult = dartResult.replace(n, ' ')
    strings = dartResult.split()
    
    score = []
    for i in range(len(numbers)):
        num = int(numbers[i])
        for string in strings[i]:
            if string == 'S':
                score.append(num**1)
            elif string == 'D':
                score.append(num**2)
            elif string == 'T':
                score.append(num**3)
            elif string == '*':
                if i != 0:
                    score[i-1] *= 2
                score[i] *= 2
            elif string == '#':
                score[i] *= -1
    return sum(score)
