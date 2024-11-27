from account.repository.account_repository_impl import AccountRepositoryImpl
from console_ui.entity.console_ui_message_state import ConsoleUiMessageState
from console_ui.repository.console_ui_repository_impl import ConsoleUiRepositoryImpl
from console_ui.service.console_ui_service import ConsoleUiService
from console_ui.user_input_handler.battle_start_user_input_handler import BattleStartUserInputHandler
from console_ui.user_input_handler.lobby_user_input_handler import LobbyUserInputHandler
from console_ui.user_input_handler.login_user_input_handler import LoginUserInputHandler
from console_ui.user_input_handler.register_user_input_handler import RegisterUserInputHandler
from game.repository.game_repository_impl import GameRepositoryImpl


class ConsoleUiServiceImpl(ConsoleUiService):
    __instance = None

    __postProcessTable = {}
    __validatationNumberLimitTable = {}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__validatationNumberLimitTable[ConsoleUiMessageState.MAIN.value] = 4
            cls.__instance.__validatationNumberLimitTable[ConsoleUiMessageState.LOBBY.value] = 4
            cls.__instance.__validatationNumberLimitTable[ConsoleUiMessageState.BATTLE_START.value] = 3

            cls.__instance.__postProcessTable[ConsoleUiMessageState.REGISTER.value] = RegisterUserInputHandler.registerForm
            cls.__instance.__postProcessTable[ConsoleUiMessageState.LOGIN.value] = LoginUserInputHandler.loginForm

            cls.__instance.__postProcessTable[ConsoleUiMessageState.LOBBY.value] = LobbyUserInputHandler.lobbyPrepareForm

            cls.__instance.__postProcessTable[ConsoleUiMessageState.BATTLE_START.value] = BattleStartUserInputHandler.battleStartForm
            # cls.__instance.__postProcessTable[ConsoleUiMessageState.BATTLE_HISTORY.value] = BattleHistoryUserInputHandler.battleHistoryForm

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

    def __validateUserInput(self, userInput, currentState):
        print(f"__validateUserInput userInput: {userInput}, currentState: {currentState}")
        validationNumber = self.__validatationNumberLimitTable[currentState]
        if userInput >= validationNumber:
            return False

        return True

    def processUserInput(self, currentState):
        userInput = self.__consoleUiRepository.processUserInput(currentState)

        userInputPostProcessTableFunction = self.__postProcessTable.get(currentState)
        if userInputPostProcessTableFunction:
            return userInputPostProcessTableFunction(userInput)

        isItValidUserInput = self.__validateUserInput(userInput, currentState)
        if isItValidUserInput is False:
            return currentState, 0

        # if currentState is ConsoleUiMessageState.REGISTER.value:
        #     accountId, password = userInput
        #     self.__accountRepository.register(accountId, password)
        #
        #     mainState = ConsoleUiMessageState.MAIN.value
        #     self.__gameRepository.updateState(mainState)
        #
        #     print("회원 가입이 완료 되었습니다!")
        #
        #     return mainState, 0
        #
        # if currentState is ConsoleUiMessageState.LOGIN.value:
        #     accountId, password = userInput
        #     isSuccess = self.__accountRepository.login(accountId, password)
        #
        #     mainState = ConsoleUiMessageState.MAIN.value
        #     lobbyState = ConsoleUiMessageState.LOBBY.value
        #     self.__gameRepository.updateState(lobbyState)
        #
        #     if isSuccess is True:
        #         print("로그인에 성공하였습니다!")
        #         return lobbyState, 0
        #
        #     print("로그인에 실패했습니다!")
        #     return mainState, 0

        return currentState, userInput
