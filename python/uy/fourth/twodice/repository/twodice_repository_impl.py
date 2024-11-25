import random
from twodice.repository.twodice_repository import TwoDiceRepository
from twodice.entity.twodice import TwoDice


class TwoDiceRepositoryImpl(TwoDiceRepository):
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
        diceNumber = random.randint(self.MIN, self.MAX)
        twodice = TwoDice(diceNumber)
        # append() 붙이기를 통해서
        # 생성자로 만든 dice를 __diceList에 추가하였습니다.
        self.__diceList.append(twodice)

        return self.__diceList

    # 누적된 전체 리스트를 가져오게 됨
    def acquireDiceList(self):
        return self.__diceList