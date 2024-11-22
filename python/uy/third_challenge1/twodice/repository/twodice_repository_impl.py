import random
from twodice.repository.twodice_repository import TwoDiceRepository
from twodice.entity.twodice import TwoDice


class TwoDiceRepositoryImpl(TwoDiceRepository):
    __instance = None
    __numList = []

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
        diceNumber1 = random.randint(self.MIN, self.MAX)
        diceNumber2 = random.randint(self.MIN, self.MAX)
        dice1 = TwoDice(diceNumber1)  # dice를 2개로 나누지 말고 하나로만 써도 ok?
        dice2 = TwoDice(diceNumber2)
        self.__numList.append(dice1)
        self.__numList.append(dice2)

    def sum(self):
        numList = self.__numList
        # numList
        # result = self.__numList.get(0).getDiceNumber() + self.get(1).getDiceNumber()
        result = 0
        for dice in self.__numList:
            result += dice.getDiceNumber()

        return result

    def acquireDiceList(self):
        return self.__numList