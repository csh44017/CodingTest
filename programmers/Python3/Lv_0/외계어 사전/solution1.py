from itertools import permutations

def solution(spell, dic):
    string = ""
    string_list = []
    for spells in list(permutations(spell, len(spell))):
        for s in spells:
            string += s
        string_list.append(string)
        string = ""

    for d in dic:
        if d in string_list:
            return 1
    return 2
