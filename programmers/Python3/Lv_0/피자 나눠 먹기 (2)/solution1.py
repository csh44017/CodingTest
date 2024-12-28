def solution(n):
    k = 1
    while True:
        pizza = 6 * k
        if pizza%n != 0:
            k = k + 1
        else:
            return k
        