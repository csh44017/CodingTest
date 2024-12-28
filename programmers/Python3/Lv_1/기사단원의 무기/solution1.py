import math

def solution(number, limit, power):
    iron = 1
    for num in range(2, number+1):
        weapon_power = 0
        root = int(math.sqrt(num))
        if root**2 == num:
            weapon_power -= 1
        for n in range(1, root+1):
            if num%n == 0:
                weapon_power += 2
            if weapon_power > limit:
                weapon_power = power
                break
        iron += weapon_power
    return iron
