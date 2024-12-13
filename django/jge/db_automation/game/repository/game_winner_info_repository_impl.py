from game.entity.game_winner_info import GameWinnerInfo
from game.repository.game_winner_info_repository import GameWinnerInfoRepository


class GameWinnerInfoRepositoryImpl(GameWinnerInfoRepository):
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

    def create(self, game, player):
        gameWinnerInfo = GameWinnerInfo(game=game, player=player)
        gameWinnerInfo.save()

        return gameWinnerInfo

    def findById(self, id):
        return GameWinnerInfo.objects.get(id=id)

    def findByGame(self, game):
        return GameWinnerInfo.objects.get(game=game)
