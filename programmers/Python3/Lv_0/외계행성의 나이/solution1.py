def solution(age):
    l = 0
    alphabet = "abcdefghij"
    result = ""
    if (age < 10):
        size = 1    
    elif (age >= 10) and (age < 100):
        size = 2
    elif (age >= 100) and (age < 1000):
        size = 3
    elif age == 1000:
        size = 4
        
    for i in range(0, size):
        num = age % (10**(i+1))
        result = alphabet[num//(10**i)] + result
    return result
    