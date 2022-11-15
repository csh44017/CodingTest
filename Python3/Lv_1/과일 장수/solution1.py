def solution(k, m, score):
    result = []
    price_list = []
    for price in range(k, 0, -1):
        apple_k = list(filter(lambda x: x==price, score))
        box = len(apple_k)//m
        result.append(price*m*box)
        price_list += apple_k[box*m:]
        
    box = len(price_list)//m
    for i in range(1, box+1):
        profit = price_list[i*m - 1] * m
        result.append(profit)
        
    return sum(result)
