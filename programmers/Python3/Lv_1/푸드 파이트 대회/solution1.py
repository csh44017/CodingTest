def solution(food):
    idx = 0
    player1 = ""
    for cnt in food:
        player1 += str(idx) * (cnt//2)
        idx += 1
    player2 = player1[::-1]
    return player1 + "0" + player2
