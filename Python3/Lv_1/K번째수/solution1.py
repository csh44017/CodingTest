def solution(array, commands):
    result = []
    for command in commands:
        arr = array[command[0]-1:command[1]]
        arr = sorted(arr)
        result.append(arr[command[2]-1])
    return result
