import random


class Dice:
        MAX = 6
        MiN = 1

        def __init__(self):
            self.__number = 0

        def rollDice(self):
            self.__number = random.randint(self.MiN, self.MAX)

            # 대문자 목적 :  python에서 대문자로하면 자동으로 private 처리가 된다
            # -> 에러 핸들링이 힘들어진다.

        def printResult(self):
            print(f"dice number : {self.__number}")