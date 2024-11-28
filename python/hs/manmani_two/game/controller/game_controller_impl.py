from console_ui.service.console_ui_service_impl import ConsoleUiServiceImpl
from game.controller.game_controller import GameController
from game.entity.game_state import GameState
from game.service.game_service_impl import GameServiceImpl


class GameControllerImpl(GameController):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__gameService = GameServiceImpl.getInstance()
            cls.__instance.__consoleUiService = ConsoleUiServiceImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def __convertNumberToState(self, currentState, userInputNumber):
        convertedStateNumber = self.__gameService.convertState(currentState, userInputNumber)
        return GameState(convertedStateNumber)

    def launchGame(self):
        self.__gameService.create()

        while True:
            currentState = self.__gameService.getState()
            if currentState == GameState.FINISH.value:
                break

            self.__consoleUiService.printMessage(currentState)
            currentState, needToProcessUserInput = self.__consoleUiService.processUserInput(currentState)
            userInputState = self.__convertNumberToState(currentState, needToProcessUserInput)
            print(f"userInputState: {userInputState}")
            self.__gameService.updateState(userInputState.value)
