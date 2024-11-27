import random

from card.entity.card import Card
from card.repository.card_repository import CardRepository


class CardRepositoryImpl(CardRepository):
    __instance = None

    __cardNumberList = []

    MIN = 1
    MAX = 10

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def pickCard(self):
        for _ in range(4):
            pickedCardNumber= random.randint(self.MIN, self.MAX)
            card = Card(int(pickedCardNumber))
            self.__cardNumberList.append(card)
            if pickedCardNumber in [3, 7]:
                count1 = self.__cardNumberList.index(card)
                print(f"You Win!: {count1}번째 뽑기에서 승리했습니다.")
                break
            if pickedCardNumber == 4:
                count2 = self.__cardNumberList.index(card)
                print(f"you lose!: {count2}번째 뽑기에서 탈락했습니다")
                break

        return self.__cardNumberList
        #return dice.getId()

    def acquireCardList(self):
        return self.__cardNumberList