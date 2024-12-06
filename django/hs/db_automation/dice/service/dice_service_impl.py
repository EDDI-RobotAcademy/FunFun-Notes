from dice.repository.dice_repository_impl import DiceRepositoryImpl
from dice.service.dice_service import DiceService
from game.repository.game_repository_impl import GameRepositoryImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl


class DiceServiceImpl(DiceService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__diceRepository = DiceRepositoryImpl.getInstance()
            cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()
            cls.__instance.__playerRepository = PlayerRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def rollDice(self, gameId, playerId):
        game = self.__gameRepository.findById(gameId)
        player = self.__playerRepository.findById(playerId)
        return self.__diceRepository.create(game, player)

    def findDice(self, requestDiceId):
        return self.__diceRepository.findById(requestDiceId)

    def findEveryDice(self):
        return self.__diceRepository.findAll()
