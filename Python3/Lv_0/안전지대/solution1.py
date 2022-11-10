import numpy as np

def solution(board):
    result = 0
    bomb = 0
    n = len(board)
    board_pad = np.pad(board, ((1, 1), (1, 1)), constant_values=0)
    for row in range(1, n+1):
        for col in range(1, n+1):
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    bomb += board_pad[row+i][col+j]
            if bomb == 0:
                result += 1
            else:    
                bomb = 0
    return result
