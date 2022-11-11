def solution(lines):    
    s1 = max(lines[0][0], lines[1][0])
    e1 = min(lines[0][1], lines[1][1])
    overlap1 = list(range(s1, e1))
    
    s2 = max(lines[1][0], lines[2][0])
    e2 = min(lines[1][1], lines[2][1])
    overlap2 = list(range(s2, e2))
    
    s3 = max(lines[0][0], lines[2][0])
    e3 = min(lines[0][1], lines[2][1])
    overlap3 = list(range(s3, e3))
    
    overlap = list(set(overlap1 + overlap2 + overlap3))
    return len(overlap)
