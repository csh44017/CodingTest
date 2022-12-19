def solution(a, b):
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    day = 0
    for m in range(a):
        day += month[m]
    return week[(day+b)%7-1]
