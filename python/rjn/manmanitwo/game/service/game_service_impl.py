from card.repository.card_repository_impl import CardRepositoryImpl
from game.repository.game_repository_impl import GameRepositoryImpl
from game.service.game_service import GameService


class gameServiceImpl(GameService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__cardRepository = CardRepositoryImpl.getInstance()
            cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def cardGameStart(self):
        print("card game Start!")

        self.__cardRepository.pickCard()

    def gameRecord(self):
        print("show me the record!")
