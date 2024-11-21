import random
# 표현하고자 하는 상태 값/ 그래서 주사위는 상수만 존재해도 ok
class Dice:
    # Constants
    MAX = 6
    MIN = 1

    # 생성자 (클래스를 만들어줌)
    def __init__(self):
        # 초기화 = 0
        self.__number = 0

    # 주사위를 굴리는 행위
    def rollDice(self):
        self.__number = random.randint(self.MIN, self.MAX)

    # 내용 출력
    def printResult(self):
        print(f"dice number: {self.__number}")