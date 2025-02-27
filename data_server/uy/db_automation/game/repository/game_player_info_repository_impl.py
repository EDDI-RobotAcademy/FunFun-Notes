from typing import List

from game.entity.game import Game
from game.entity.game_player_info import GamePlayerInfo
from game.repository.game_player_info_repository import GamePlayerInfoRepository
from player.entity.player import Player


class GamePlayerInfoRepositoryImpl(GamePlayerInfoRepository):
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
        gamePlayerInfo = GamePlayerInfo(game=game, player=player)
        gamePlayerInfo.save()

        return gamePlayerInfo

    def findById(self, id):
        return GamePlayerInfo.objects.get(id=id)

    def findByGame(self, game):
        return GamePlayerInfo.objects.filter(game=game)

    def findPlayerListByGame(self, game: Game) -> List[Player]:
        gamePlayerInfo = GamePlayerInfo.objects.filter(game=game)
        playerList = [gamePlayerInfo.getPlayer() for gamePlayerInfo in gamePlayerInfo]

        return playerList
