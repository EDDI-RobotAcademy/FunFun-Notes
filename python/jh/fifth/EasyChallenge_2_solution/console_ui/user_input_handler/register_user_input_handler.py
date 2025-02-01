from account.repository.account_repository_impl import AccountRepositoryImpl
from console_ui.entity.console_ui_message_state import ConsoleUiMessageState
from game.repository.game_repository_impl import GameRepositoryImpl


class RegisterUserInputHandler:
    __accountRepository = AccountRepositoryImpl.getInstance()
    __gameRepository = GameRepositoryImpl.getInstance()

    @classmethod
    def registerForm(self, userInput):
        accountId, password = userInput
        self.__accountRepository.register(accountId, password)

        mainState = ConsoleUiMessageState.MAIN.value
        self.__gameRepository.updateState(mainState)

        print("회원 가입이 완료 되었습니다!")

        return mainState, 0
