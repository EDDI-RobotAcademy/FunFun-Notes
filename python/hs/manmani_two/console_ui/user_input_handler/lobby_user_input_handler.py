from account.repository.account_repository_impl import AccountRepositoryImpl
from console_ui.entity.console_ui_message_state import ConsoleUiMessageState
from deck.repository.deck_repository_impl import DeckRepositoryImpl
from game.repository.game_repository_impl import GameRepositoryImpl
from record.repository.record_repository_impl import RecordRepositoryImpl
from turn.repository.turn_repository_impl import TurnRepositoryImpl


class LobbyUserInputHandler:
    __accountRepository = AccountRepositoryImpl.getInstance()
    __gameRepository = GameRepositoryImpl.getInstance()
    __deckRepository = DeckRepositoryImpl.getInstance()
    __turnRepository = TurnRepositoryImpl.getInstance()
    __recordRepository = RecordRepositoryImpl.getInstance()

    @classmethod
    def lobbyPrepareForm(self, userInput):
        mainState = ConsoleUiMessageState.MAIN.value
        lobbyState = ConsoleUiMessageState.LOBBY.value
        battleStartState = ConsoleUiMessageState.BATTLE_START.value

        self.__deckRepository.create()
        self.__turnRepository.create()
        self.__gameRepository.updateState(battleStartState)

        if userInput == 2:
            currentSingInAccountId = self.__accountRepository.getCurrentSignInUserId()
            recordList = self.__recordRepository.getRecordList()
            for record in recordList:
                accountUniqueId = record.getAccountUniqueId()
                if currentSingInAccountId != accountUniqueId:
                    continue

                account = self.__accountRepository.findById(accountUniqueId)

                print(f"Account ID: {account.getAccountId()}, Record Turn Count: {record.getTurnCountNumber()}, Win: {record.getIsWin()}")

            return lobbyState, 0

        if userInput == 3:
            return mainState, 0

        return battleStartState, 0
