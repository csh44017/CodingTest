def solution(my_string):
    math_list = my_string.split()
    result = int(math_list.pop(0))
    length = len(math_list) // 2
    for l in range(length):
        calc = math_list[2*l]
        num = int(math_list[2*l+1])
        if calc == "+":
            result += num
        elif calc == "-":
            result -= num
    return result
