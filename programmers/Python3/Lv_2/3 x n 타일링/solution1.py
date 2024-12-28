def solution(n):
    if n%2: return 0

    mem = [0] * (n+1)
    mem[2], mem[4] = 3, 11
    temp = mem[2]
    for i in range(6, n+1, 2):
        mem[i] = (mem[i-2]*3 + temp*2 + 2) % 1000000007
        temp += mem[i-2]
    return mem[n]
