import random
from third.dice.entity.dice import Dice
from third.dice.repository.dice_repository import DiceRepository

class DiceRepositoryImpl(DiceRepository):

    __instance = None

    # 우리가 굴린 주사위의 리스트/결과를 관리하기 위함임
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
            # 이 부분에서 실질적으로 __new__ 이 호출됨
            cls.__instance = cls()

        return cls.__instance


    def rollDice(self):
        diceNumber = random.randint(self.MIN, self.MAX)  # MIN - MAX 사이의 랜덤값 추출
        dice = Dice(diceNumber)
        # append() 붙이기를 통해서
        # 생성자로 만든 dice를 __diceList에 추가
        self.__diceList.append(dice)

    # 누적된 전체 리스트를 가져오게 됨
    def acquireDiceList(self):

        return self.__diceList
