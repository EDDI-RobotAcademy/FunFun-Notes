from game.entity.game import Game
from game.entity.game_state import GameState
from game.repository.game_repository import GameRepository


class GameRepositoryImpl(GameRepository):
    __instance = None
    __game = None

    __convertTable = {}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__convertTable[GameState.MAIN.value] = {}
            cls.__instance.__convertTable[GameState.MAIN.value][0] = GameState.MAIN.value
            cls.__instance.__convertTable[GameState.MAIN.value][1] = GameState.REGISTER.value
            cls.__instance.__convertTable[GameState.MAIN.value][2] = GameState.LOGIN.value

            cls.__game = Game()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self):
        self.__game.updateState(GameState.MAIN.value)

    def getState(self):
        return self.__game.getState()

    def convertState(self, currentState, userInputNumber):
        return self.__convertTable[currentState][userInputNumber]

    def updateState(self, state):
        self.__game.updateState(state)
