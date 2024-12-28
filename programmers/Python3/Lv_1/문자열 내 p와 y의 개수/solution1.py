def solution(s):
    cnt_p = s.count('p') + s.count('P')
    cnt_y = s.count('y') + s.count('Y')
    if cnt_p == 0 and cnt_y == 0:
        return True
    if cnt_p == cnt_y:
        return True
    else:
        return False
    