def solution(answers):
    student1 = [1, 2, 3, 4, 5] * (len(answers)//5 + 1)
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers)//8 + 1)
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//10 + 1)
    
    scores = [0, 0, 0]
    for i in range(len(answers)):
        if student1[i] == answers[i]:
            scores[0] += 1
        if student2[i] == answers[i]:
            scores[1] += 1
        if student3[i] == answers[i]:
            scores[2] += 1
    max_score = max(scores[0], scores[1], scores[2])

    result = []
    for idx, score in enumerate(scores):
        if score == max_score:
            result.append(idx+1)
    return result
