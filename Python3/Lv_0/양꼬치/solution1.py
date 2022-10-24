def solution(n, k):
    food = 12000 * n
    beverage = 2000 * (k - n//10)
    return food + beverage
