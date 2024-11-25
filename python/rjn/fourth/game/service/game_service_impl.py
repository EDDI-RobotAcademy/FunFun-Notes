from dice.repository.dice_repository_impl import DiceRepositoryImpl
from game.repository.game_repository_impl import GameRepositoryImpl
from game.service.game_service import GameService
from player.repository.player_repository_impl import PlayerRepositoryImpl


class GameServiceImpl(GameService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            # Service Layer에서 Repository Layer를 연결하는 방법
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
        self.__diceRepository.rollDice()
        eachPlayerDiceList = self.__diceRepository.rollDice()

        self.__gameRepository.start(
            playerNameList, eachPlayerDiceList)

    def checkWinner(self):
        print("checkWinner() called!")
        self.__gameRepository.checkWinner()
