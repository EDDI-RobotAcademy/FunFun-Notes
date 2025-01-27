from game.service.game_service import GameService
from game.repository.game_repository_impl import GameRepositoryImpl
from dice.repository.dice_repository_impl import DiceRepositoryImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl


class GameServiceImpl(GameService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()
            cls.__instance.__playerRepository = PlayerRepositoryImpl.getInstance()
            cls.__instance.__diceRepository = DiceRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def startDiceGame(self):
        print("startDiceGame() called!")
        playerNameList = self.__playerRepository.acquirePlayerNameList()
        for i in range(len(playerNameList)):
            self.__diceRepository.rollDice()
        eachPlayerDiceList = self.__diceRepository.acquireDiceList()

        self.__gameRepository.start(
            playerNameList, eachPlayerDiceList)

    def checkWinner(self):
        print("checkWinner() called!")
        self.__gameRepository.checkWinner()
