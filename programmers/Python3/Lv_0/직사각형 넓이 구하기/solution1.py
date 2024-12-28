def solution(dots):
    x1 = dots[0][0]
    y1 = dots[0][1]
    for dot in dots:
        if dot[0] != x1:
            x = x1 - dot[0]
        if dot[1] != y1:
            y = y1 - dot[1]
    return abs(x*y)
