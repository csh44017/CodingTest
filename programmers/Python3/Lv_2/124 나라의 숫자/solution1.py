def solution(n):
    answer = ""
    while n:
        mod = n%3
        if not mod:
            mod = 3
            n -= 1
        n //= 3
        answer = str(mod) + answer
    answer = answer.replace('3', '4')
    return answer
