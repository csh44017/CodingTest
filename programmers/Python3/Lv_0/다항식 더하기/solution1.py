def solution(polynomial):
    coef, const = 0, 0
    for p in polynomial.split(" + "):
        if "x" in p:
            if p == "x":
                coef += 1
            else:
                coef += int(p[:-1])
        else:
            const += int(p)
    
    if (coef == 0) and (const == 0):
        return "0"
    elif (coef > 1) and (const != 0):
        return str(coef) + "x + " + str(const)
    elif (coef == 1) and (const != 0):
        return "x + " + str(const)
    elif (coef > 1) and (const == 0):
        return str(coef) + "x"
    elif (coef == 1) and (const == 0):
        return "x"
    elif (coef == 0) and (const != 0):
        return str(const)
