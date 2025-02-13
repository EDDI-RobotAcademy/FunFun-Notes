from account.repository.account_repository_impl import AccountRepositoryImpl
from console_ui.entity.console_ui_message_state import ConsoleUiMessageState
from deck.repository.deck_repository_impl import DeckRepositoryImpl
from game.repository.game_repository_impl import GameRepositoryImpl
from record.repository.record_repository_impl import RecordRepositoryImpl
from turn.repository.turn_repository_impl import TurnRepositoryImpl


class BattleStartUserInputHandler:
    __accountRepository = AccountRepositoryImpl.getInstance()
    __gameRepository = GameRepositoryImpl.getInstance()
    __deckRepository = DeckRepositoryImpl.getInstance()
    __turnRepository = TurnRepositoryImpl.getInstance()
    __recordRepository = RecordRepositoryImpl.getInstance()

    @classmethod
    def battleStartForm(self, userInput):
        print(f"battleStartForm userInput: {userInput}")

        battleStartState = ConsoleUiMessageState.BATTLE_START.value
        lobbyState = ConsoleUiMessageState.LOBBY.value

        turn = self.__turnRepository.getTurn()
        currentTurnNumber = turn.getTurnCount()

        if userInput == 2:
            print("패배")
            currentSignInUserId = self.__accountRepository.getCurrentSignInUserId()
            self.__recordRepository.create(currentSignInUserId, currentTurnNumber, False)
            return lobbyState, 0

        drawCardNumber = self.__deckRepository.drawCard()
        print(f"뽑은 카드: {drawCardNumber}")

        if drawCardNumber == 4:
            print("패배")
            currentSignInUserId = self.__accountRepository.getCurrentSignInUserId()
            self.__recordRepository.create(currentSignInUserId, currentTurnNumber, False)
            return lobbyState, 0

        if drawCardNumber in [3, 7]:
            print("승리!")
            currentSignInUserId = self.__accountRepository.getCurrentSignInUserId()
            self.__recordRepository.create(currentSignInUserId, currentTurnNumber, True)
            return lobbyState, 0

        self.__gameRepository.updateState(battleStartState)
        self.__turnRepository.addTurnCount()

        if currentTurnNumber >= 4:
            print("패배")
            currentSignInUserId = self.__accountRepository.getCurrentSignInUserId()
            self.__recordRepository.create(currentSignInUserId, currentTurnNumber, False)
            return lobbyState, 0

        return battleStartState, 0
