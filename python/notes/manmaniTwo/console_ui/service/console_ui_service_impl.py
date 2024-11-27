from account.repository.account_repository_impl import AccountRepositoryImpl
from console_ui.entity.console_ui_message_state import ConsoleUiMessageState
from console_ui.repository.console_ui_repository_impl import ConsoleUiRepositoryImpl
from console_ui.service.console_ui_service import ConsoleUiService
from game.repository.game_repository_impl import GameRepositoryImpl


class ConsoleUiServiceImpl(ConsoleUiService):
    __instance = None

    __postProcessTable = {}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def printMessage(self, state):
        self.__consoleUiRepository.printMessage(state)

    def processUserInput(self, currentState):
        userInput = self.__consoleUiRepository.processUserInput(currentState)
        if currentState is ConsoleUiMessageState.REGISTER.value:
            accountId, password = userInput
            self.__accountRepository.register(accountId, password)

            mainState = ConsoleUiMessageState.MAIN.value
            self.__gameRepository.updateState(mainState)

            print("회원 가입이 완료 되었습니다!")

            return mainState, 0

        if currentState is ConsoleUiMessageState.LOGIN.value:
            accountId, password = userInput
            isSuccess = self.__accountRepository.login(accountId, password)

            mainState = ConsoleUiMessageState.MAIN.value
            self.__gameRepository.updateState(mainState)

            if isSuccess is True:
                print("회원 가입이 완료 되었습니다!")
            else:
                print("로그인에 실패했습니다!")

            return mainState, 0

        return currentState, userInput
