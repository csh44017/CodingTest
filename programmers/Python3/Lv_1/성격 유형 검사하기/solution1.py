def solution(survey, choices):
    case = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    length = len(survey)
    for i in range(length):
        score = choices[i]-4
        if score < 0:
            char = survey[i][0]
            case[char] += abs(score)
        elif score > 0:
            char = survey[i][1]
            case[char] += abs(score)
            
    result = ""
    if case['R'] >= case['T']:
        result += "R"
    else:
        result += "T"
    if case['C'] >= case['F']:
        result += "C"
    else:
        result += "F"
    if case['J'] >= case['M']:
        result += "J"
    else:
        result += "M"
    if case['A'] >= case['N']:
        result += "A"
    else:
        result += "N"
    return result
