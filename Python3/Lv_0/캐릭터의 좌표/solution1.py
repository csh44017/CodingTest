def solution(keyinput, board):
    pos = [0, 0]
    max_x = (board[0]-1)//2
    max_y = (board[1]-1)//2
    for key in keyinput:
        if (key == "up") and (pos[1] < max_y):
            pos[1] += 1
        elif (key == "down") and (pos[1] > -max_y):
            pos[1] -= 1
        elif (key == "left") and (pos[0] > -max_x):
            pos[0] -= 1
        elif (key == "right") and (pos[0] < max_x):
            pos[0] += 1
    return pos
