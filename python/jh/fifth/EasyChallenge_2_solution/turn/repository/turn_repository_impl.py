from turn.entity.turn import Turn
from turn.repository.turn_repository import TurnRepository


class TurnRepositoryImpl(TurnRepository):
    __instance = None
    __turn = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getTurn(self):
        return self.__turn

    def create(self):
        self.__turn = Turn()

    def addTurnCount(self):
        self.__turn.addTurnCount()
    