def solution(nums):
    max_len = len(set(nums))
    choice = len(nums)//2
    if choice > max_len:
        return max_len
    else:
        return choice
    