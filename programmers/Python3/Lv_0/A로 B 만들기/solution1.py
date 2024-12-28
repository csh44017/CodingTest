def solution(before, after):
    for b in before:
        after = after.replace(b, "", 1)
    if len(after) == 0:
        return 1
    else:
        return 0
    