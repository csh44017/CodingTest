import string

tmp = string.digits
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r] 
    else:
        return convert(q, base) + tmp[r]

def solution(n):
    n_str = ""
    n = convert(n, 3)
    for num in reversed(n):
        n_str += num
    return int(n_str, 3)
