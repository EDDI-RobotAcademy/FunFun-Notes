from deck.entity.deck import Deck
from deck.repository.deck_repository import DeckRepository


class DeckRepositoryImpl(DeckRepository):
    __instance = None
    __deck = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self):
        self.__deck = Deck()

    def drawCard(self):
        if not self.__deck:
            raise ValueError("create()을 호출하여 덱 초기화를 먼저해주세요.")

        cardMap = self.__deck.getCardMap()

        for cardNumber, isUsed in cardMap.items():
            if not isUsed:
                cardMap[cardNumber] = True
                return cardNumber

        raise ValueError("더 이상 뽑을 카드가 존재하지 않습니다.")
