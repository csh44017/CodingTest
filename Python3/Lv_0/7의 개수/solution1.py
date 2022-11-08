def solution(array):
    num_str = ""
    for arr in array:
        num_str += str(arr)
    return num_str.count("7")
