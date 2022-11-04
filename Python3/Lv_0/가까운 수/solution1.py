import numpy as np

def solution(array, n):
    close = 101
    result = 101
    for num in array:
        diff_abs = np.abs(num - n)
        if diff_abs < close:
            close = diff_abs
            result = num
        elif diff_abs == close:
            if num < result:
                result = num
    return result
