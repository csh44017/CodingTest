def solution(dots):
    gradients = []
    length = len(dots)
    for row in range(length-1):
        for i in range(row+1, length):
            delta_y = dots[row][1] - dots[i][1]
            delta_x = dots[row][0] - dots[i][0]
            if delta_x != 0:
                gradient = delta_y / delta_x

                if not gradient in gradients:
                    gradients.append(gradient)
                else:
                    return 1
    return 0
