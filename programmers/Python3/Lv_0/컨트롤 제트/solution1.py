def solution(s):
    num_list = []    
    for string in s.split(' '):
        if string == "Z":
            num_list.pop()
        else:
            num_list.append(int(string))
    return sum(num_list)
