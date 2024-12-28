def solution(absolutes, signs):
    result = 0
    for i in range(len(signs)):
        if signs[i]:
            result += int(absolutes[i])
        else:
            result -= int(absolutes[i])
    return result
