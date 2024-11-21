import random
#random함수를 사용하기 위해 정의
class Dice:
    MAX = 6
    MIN = 1
    #MIN과MAX에 각 값을 주입

    def __init__(self, diceNumber):
        self.__number = diceNumber
        #self값 초기화 후 __number 대입 거기에 diceNumber값 주입

    def printResult(self):
        print(f"dice number: {self.__number}")
        #__number값 출력

    def getDiceNumber(self):
        return self.__number
    #__number값 가져오기