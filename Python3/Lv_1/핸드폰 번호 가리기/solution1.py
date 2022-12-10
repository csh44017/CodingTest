def solution(phone_number):
    blind = '*' * len(phone_number[:-4])
    return blind + phone_number[-4:]
