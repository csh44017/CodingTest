def solution(hp):
    ant5 = hp//5
    ant3 = (hp - ant5 * 5)//3
    ant1 = (hp - ant5 * 5)%3
    return ant5+ant3+ant1
