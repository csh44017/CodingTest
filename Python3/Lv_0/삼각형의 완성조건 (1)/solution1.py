def solution(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (a < b+c) and (b < c+a) and (c < a+b):
        return 1
    else:
        return 2
    