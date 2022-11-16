def solution(ingredient):
    idx = 0
    hamburger = 0
    while True:        
        is_take = ingredient[idx:idx+4] == [1, 2, 3, 1]
        if is_take:
            hamburger += 1
            for _ in range(4):
                ingredient.pop(idx)
                
            if idx < 4:
                idx = 0
            else:
                idx -= 3
        else:
            idx += 1

        if idx >= len(ingredient):
            return hamburger
