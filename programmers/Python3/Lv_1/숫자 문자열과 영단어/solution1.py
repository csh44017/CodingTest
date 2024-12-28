def solution(s):
    str = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    for i in range(10):
        s = s.replace(str[i], num[i])
    return int(s)
