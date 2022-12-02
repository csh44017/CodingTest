def solution(board, moves):
    result = 0
    basket = [-1]
    for col in moves:
        row = 0
        while row < len(board):
            doll = board[row][col-1]
            if doll > 0:
                board[row][col-1] = 0
                if basket[-1] == doll:
                    basket = basket[:-1]
                    result += 1
                    break
                else:
                    basket.append(doll)
                    break
            row += 1
    return result
