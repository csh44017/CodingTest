def solution(numbers, hand):
    result = ""
    coordinate = [(4,2), (1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)]
    left_hand = (4,1)
    right_hand = (4,3)
    for n in numbers:
        if n in [1, 4, 7]:
            result += 'L'
            left_hand = coordinate[n]
        elif n in [3, 6, 9]:
            result += 'R'
            right_hand = coordinate[n]
        else:
            left_dist = abs(left_hand[0]-coordinate[n][0]) + abs(left_hand[1]-coordinate[n][1])
            right_dist = abs(right_hand[0]-coordinate[n][0]) + abs(right_hand[1]-coordinate[n][1])
            if left_dist > right_dist:
                result += 'R'
                right_hand = coordinate[n]
            elif left_dist == right_dist:
                if hand == "left":
                    result += 'L'
                    left_hand = coordinate[n]
                elif hand == "right":
                    result += 'R'
                    right_hand = coordinate[n]
            else:
                result += 'L'
                left_hand = coordinate[n]
    return result
