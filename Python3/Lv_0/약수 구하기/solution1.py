def solution(n):
    front = []
    back = []
    root = int(n**(1/2))
    for i in range(1, root+1):
        if (n%i == 0) and (i*i != n):
            front.append(i)
    if root*root == n:
        back.append(root)
    for f in list(reversed(front)):
        back.append(n/f)
    return front + back
