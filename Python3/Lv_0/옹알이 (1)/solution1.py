from itertools import permutations

def solution(babbling):
    pronunciation = []
    speak = ["aya", "ye", "woo", "ma"]
    for l in range(1, len(speak)+1):
        for spk in list(permutations(speak, l)):
            speaks = ""
            for s in spk:
                speaks += s
            pronunciation.append(speaks)
    cnt = 0
    for b in babbling:
        if b in pronunciation:
            cnt += 1
    return cnt
