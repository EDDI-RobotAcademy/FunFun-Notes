import random
from card.entity.card import Card
from card.repository.card_repository import CardRepository


class CardRepositoryImpl(CardRepository):
    __instance = None

    MIN = 1
    MAX = 10
    __cardList = []

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
        cardNumber = random.randint(self.MIN, self.MAX)
        card = Card(cardNumber)
        self.__cardList.append(card)
        return card

    def getAcquiredCardList(self):
        return self.__cardList
