def solution(denum1, num1, denum2, num2):
    denum = (denum1*num2) + (denum2*num1)
    num = num1*num2
    common = 0
    for k in range(1, denum+1):
        if (denum%k == 0) and (num%k == 0):
            common = k
    return [denum/common, num/common]
