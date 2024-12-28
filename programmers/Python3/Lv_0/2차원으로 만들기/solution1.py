import numpy as np

def solution(num_list, n):
    row = len(num_list) // n
    result = np.array(num_list).reshape((row, n))
    return result.tolist()
