def solution(bin1, bin2):
    binary1 = int(bin1, 2)
    binary2 = int(bin2, 2)
    return bin(binary1 + binary2)[2:]
