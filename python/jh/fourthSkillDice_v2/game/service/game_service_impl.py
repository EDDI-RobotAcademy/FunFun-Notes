from dice.repository.dice_repository_impl import DiceRepositoryImpl
from game.repository.game_repository_impl import GameRepositoryImpl
from game.service.game_service import GameService
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

    def __createGamePlayer(self):
        gamePlayerCount = self.__gameRepository.gamePlayerCount()

        for _ in range(gamePlayerCount):
            self.__playerRepository.createName()

    def startDiceGame(self):
        print("startDiceGame() called!")
        self.__gameRepository.create()

        self.__createGamePlayer()

    def printCurrentStatus(self):
        pass

    def rollFirstDice(self):
        gamePlayerCount = self.__gameRepository.gamePlayerCount()
        playerIndexList = []
        diceIdList = []


        for playerIndex in range(gamePlayerCount):
            print(f"playerIndex: {playerIndex}")
            diceId = self.__diceRepository.rollDice()
            diceIdList.append(diceId)

            indexedPlayer = self.__playerRepository.findById(playerIndex + 1)
            print(f"indexedPlayer: {indexedPlayer}")

            playerIndexList.append(playerIndex + 1)

            indexedPlayer.addDiceId(diceId)

        for player in self.__playerRepository.acquirePlayerList():
            print(f"{player}")







            9
