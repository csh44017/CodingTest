def solution(a, b, n):
    service = (n//a)*b
    n = n%a + service
    result = service
    
    while n >= a:
        service = (n//a)*b
        n = n%a + service
        result += service
    return result
