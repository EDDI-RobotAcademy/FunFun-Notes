from mypy.binder import defaultdict

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
            cls.__instance.__diceRepository = DiceRepositoryImpl.getInstance()
            cls.__instance.__playerRepository = PlayerRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createGame(self):
        self.__gameRepository.create()

    def checkWinner(self, gameId):
        game = self.__gameRepository.findById(gameId)
        print(f"checkWinner -> game: {game}")
        diceList = self.__diceRepository.findByGameId(game)
        print(f"checkWinner -> diceList: {diceList}")

        playerScoreDictionary = defaultdict(int)

        for dice in diceList:
            playerScoreDictionary[dice.player.id] += dice.number

        maxScore = max(playerScoreDictionary.values())
        winnerList = [playerId for playerId, score in playerScoreDictionary.items()
                      if score == maxScore]

        if len(winnerList) == 1:
            winnerId = winnerList[0]
            winner = self.__playerRepository.findById(winnerId)

            loserList = [playerId for playerId in playerScoreDictionary.keys()
                         if playerId != winnerId]
            loserId = loserList[0]

            self.__gameRepository.update(gameId, winnerId, loserId, GameState.WIN)


            return f"승자: {winner}, 승자 점수: {maxScore}"

        self.__gameRepository.update(gameId, winnerId, loserId, GameState.DRAW)
        return f"무승부, 점수: {maxScore}"





