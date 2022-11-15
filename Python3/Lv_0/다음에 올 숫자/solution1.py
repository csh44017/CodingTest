def solution(common):
    n1, n2, n3 = common[0], common[1], common[2]
    if n2-n1 == n3-n2:
        return common[-1] + (n2-n1)
    else:
        return common[-1]*(n2//n1)
    