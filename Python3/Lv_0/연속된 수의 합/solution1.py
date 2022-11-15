def solution(num, total):
    sigma_num = 0
    for n in range(1, num+1):
        sigma_num += n
    
    add = 0
    while sigma_num + num*add != total:
        sigma = sigma_num + num*add
        if sigma < total:
            add += 1
        elif sigma > total:
            add -= 1
        
    result = []
    for n in range(1, num+1):
        result.append(n+add)
    return result
