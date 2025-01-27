import random

from dice.entity.dice import Dice
from dice.repository.dice_repository import DiceRepository


class DiceRepositoryImpl(DiceRepository):
    __instance = None

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
        diceNum = random.randint(self.MIN, self.MAX)
        dice = Dice(diceNum)
        self.__diceList.append(dice)

        return self.__diceList
                # return 값 생략 가능 해당 클래스 메서드가 호출되면서
                     #  클래스 변수로 선언된 리스트가 return으로 명시하지 않아도 업데이트 된다.

    def getDiceList(self):
        return self.__diceList


