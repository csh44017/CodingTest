def solution(id_list, report, k):
    user = {}
    mail = {}
    for id in id_list:
        user[id] = 0
        mail[id] = 0
        
    report = list(set(report))
    for r in report:
        user[r.split()[1]] += 1
    for r in report:
        if user[r.split()[1]] >= k:
            mail[r.split()[0]] += 1

    result = []
    for id in id_list:
        result.append(mail[id])
    return result
