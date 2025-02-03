from console_ui.repository.console_ui_repository_impl import ConsoleUiRepositoryImpl
from game.entity.game_state import GameState
from game.repository.game_repository_impl import GameRepositoryImpl
from game.service.game_service import GameService


class GameServiceImpl(GameService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()
            cls.__instance.__consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def __convertNumberToState(self, userInputNumber):
        currentState = self.__gameRepository.getState()
        convertedStateNumber = self.__gameRepository.convertState(currentState, userInputNumber)
        return GameState(convertedStateNumber)

    # def launchGame(self):
    #     self.__gameRepository.create()
    #
    #     while True:
    #         currentState = self.__gameRepository.getState()
    #         if currentState == GameState.FINISH.value:
    #             break
    #
    #         self.__consoleUiRepository.printMessage(currentState)
    #         userInput = self.__consoleUiRepository.processUserInput(currentState)
    #         userInputState = self.__convertNumberToState(userInput)
    #         # print(f"userInputState: {userInputState}")
    #         self.__gameRepository.updateState(userInputState.value)

    def create(self):
        self.__gameRepository.create()

    def getState(self):
        return self.__gameRepository.getState()

    def convertState(self, currentState, userInputNumber):
        return self.__gameRepository.convertState(currentState, userInputNumber)

    def updateState(self, state):
        self.__gameRepository.updateState(state)
