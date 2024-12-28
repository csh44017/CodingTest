def solution(rsp):
    result = ""
    for random in rsp:
        if random == "2":
            result = result + "0"
        elif random == "0":
            result = result + "5"
        elif random == "5":
            result = result + "2"
    return result
