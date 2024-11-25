import random

from dice.entity.dice import Dice
from dice.repository.dice_repository import DiceRepository


class DiceRepositoryImpl(DiceRepository):
    __instance = None

    # 빈 리스트를 생성하여 여기에 주사위 정보를 저장하려고 함
    # 즉 이번 케이스는 rollDice()가 구동 될 때마다 diceList에 내용이 누적됨
    __diceList = []

    MIN = 1
    MAX = 6

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def rollDice(self):
        diceNumber = random.randint(self.MIN, self.MAX)
        dice = Dice(diceNumber)
        self.__diceList.append(dice)
        #append()

    # 누적된 전체 리스트를 가져오게 됨
    def acquireDiceList(self):
        return self.__diceList

    def sumEveryDiceNumber(self):
        diceSumNumber = 0

        for dice in self.__diceList:
            number = dice.getDiceNumber()
            diceSumNumber += number

        return diceSumNumber

# class diceSummation:
#     @staticmethod
#     def calculateSum(diceList):
#         total = sum(dice.number for dice in diceList)  # Dice 객체의 number 속성을 합산
#         print(f"주사위의 눈금의 합은: {total}")  # 합산 결과 출력
#         #return total  # 합산 결과 반환
#         #total = sum(dice.number for dice in diceList)
