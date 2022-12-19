def solution(arr):
    before = -1
    answer = []
    for num in arr:
        if num != before:
            answer.append(num)
            before = num
    return answer
