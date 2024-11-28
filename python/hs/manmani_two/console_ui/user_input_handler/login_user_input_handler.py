from account.repository.account_repository_impl import AccountRepositoryImpl
from console_ui.entity.console_ui_message_state import ConsoleUiMessageState
from game.repository.game_repository_impl import GameRepositoryImpl


class LoginUserInputHandler:
    __accountRepository = AccountRepositoryImpl.getInstance()
    __gameRepository = GameRepositoryImpl.getInstance()

    @classmethod
    def loginForm(self, userInput):
        accountId, password = userInput
        isSuccess = self.__accountRepository.login(accountId, password)

        mainState = ConsoleUiMessageState.MAIN.value
        lobbyState = ConsoleUiMessageState.LOBBY.value
        self.__gameRepository.updateState(lobbyState)

        if isSuccess is True:
            print("로그인에 성공하였습니다!")
            return lobbyState, 0

        print("로그인에 실패했습니다!")
        return mainState, 0
