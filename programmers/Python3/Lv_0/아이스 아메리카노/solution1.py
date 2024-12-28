def solution(money):
    americano = money//5500
    balance = money%5500
    return [americano, balance]
