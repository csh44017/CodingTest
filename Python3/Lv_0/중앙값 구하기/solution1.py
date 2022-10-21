def solution(array):
    length = len(array)
    for n in range(length-1):
        for m in range(n, length):
            if array[n] > array[m]:
                temp = array[m]
                array[m] = array[n]
                array[n] = temp
        n = n+1
    return array[length//2]
