import random


class Dice:
    # 클래스 생성시 class 키워드를 붙여야합니다.
    # 생성하고자 하는 클래스 이름은 Dice입니다.
    #사실상 class를 Domain 바라봐야합니다.
    #

        MAX = 6
        MiN = 1
    #보편적으로 대문자로만 적는 것들 (상수값)

        #init 생성자
        def __init__(self):
            self.__number = 0

        def rollDice(self):
            self.__number = random.randint(self.MiN, self.MAX)

            # 대문자 목적 :  python에서 대문자로하면 자동으로 private 처리가 된다
            # -> 에러 핸들링이 힘들어진다.

        def printResult(self):
            print(f"dice number : {self.__number}")