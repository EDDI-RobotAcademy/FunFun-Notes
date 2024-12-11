from game.entity.game import Game
from game.repository.game_repository import GameRepository


class GameRepositoryImpl(GameRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, playerCount):
        game = Game(playerCount=playerCount)
        game.save()

        return game

    def findById(self, id):
        return Game.objects.get(id=id)

    def update(self, game, gameState):
        game.setState(gameState)
        game.save()

        return game

