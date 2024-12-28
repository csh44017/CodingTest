def solution(array, height):
    cnt = 0
    for tall in array:
        if tall > height:
            cnt = cnt + 1
    return cnt
