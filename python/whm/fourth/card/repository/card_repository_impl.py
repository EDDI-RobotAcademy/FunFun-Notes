from card.repository.card_repository import CardRepository
from card.entity.card import Card
import random

class CardRepositoryImpl(CardRepository):
    __instance=None
    __cardList=[1,2,3,4,5,6,7,8,9,10]
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance=super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance=cls()

        return cls.__instance
    #싱글톤

    def selectCard(self):
        while True:
            user=input("카드를 뽑겠습니까?")
            if user=="yes":
                card=random.choice(self.__cardList)
                myCard=Card(card)
                self.__cardList.remove(card)
                print(myCard)
                print(self.__cardList)

                return myCard.getNumber()

            else:
                print("yes말고는 없습니다")
                continue