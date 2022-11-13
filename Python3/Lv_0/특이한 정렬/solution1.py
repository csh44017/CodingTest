def solution(numlist, n):        
    def distance(num):
        return abs(num-n)
    dist = list(map(distance, numlist))
    dist.sort()
    
    result = []
    numlist.sort(reverse=True)
    for d in dist:
        for num in numlist:
            if abs(num-n) == d:
                result.append(num)
                numlist.remove(num)
    return result
