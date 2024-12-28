def solution(n, m):
    large = max(n, m)
    small = min(n, m)
    result = [0, large]

    for num in range(small, 0, -1):
        if large%num == 0 and small%num == 0:
            result[0] = num
            break
        
    while result[1]%large != 0 or result[1]%small != 0:
        result[1] += large
    
    return result
