def solution(board):
    row, col = len(board), len(board[0])
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                
    answer = 0
    for i in range(row):
        temp = max(board[i])
        answer = max(answer, temp)
    return answer**2
