import random


# Entity: Dice 클래스
class Dice:
    def __init__(self):
        self.number = 0  # 주사위 눈금, 초기값은 0

    def roll(self):
        """주사위 굴리기"""
        self.number = random.randint(1, 6)  # 1부터 6까지의 랜덤 값
