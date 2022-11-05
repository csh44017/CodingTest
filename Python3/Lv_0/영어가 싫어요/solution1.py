def solution(numbers):
    result = ""
    number = ""
    for n in numbers:
        number += n
        if number == "zero":
            result += "0"
            number = ""
        elif number == "one":
            result += "1"
            number = ""
        elif number == "two":
            result += "2"
            number = ""
        elif number == "three":
            result += "3"
            number = ""
        elif number == "four":
            result += "4"
            number = ""
        elif number == "five":
            result += "5"
            number = ""
        elif number == "six":
            result += "6"
            number = ""
        elif number == "seven":
            result += "7"
            number = ""
        elif number == "eight":
            result += "8"
            number = ""
        elif number == "nine":
            result += "9"
            number = ""
    return int(result)
