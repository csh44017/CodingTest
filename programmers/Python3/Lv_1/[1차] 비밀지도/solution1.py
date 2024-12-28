def solution(n, arr1, arr2):
    result = []
    for array1, array2 in zip(arr1, arr2):
        encode1 = bin(array1)[2:].zfill(n)
        encode2 = bin(array2)[2:].zfill(n)
        row = ""
        for decode1, decode2 in zip(encode1, encode2):
            if int(decode1) + int(decode2) == 0:
                row += ' '
            else:
                row += '#'
        result.append(row)        
    return result
