from game.entity.game import Game
from game.repository.game_repository import GameRepository


class GameRepositoryImpl(GameRepository):
    __instance = None

    __gameList = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def start(self, playerNameList, eachPlayerDiceList):
        game = Game(playerNameList, eachPlayerDiceList)
        self.__gameList.append(game)

    def checkWinner(self):
        game = self.__gameList[0]
        gameMapInfo = game.getGameMap()

        # Dictionary의 key 값 다 뽑기
        gameMapKeyList = gameMapInfo.keys()
        # Dictionary의 value 값 다 뽑기
        gameMapValueList = gameMapInfo.values()
        # Dictionary의 key, value 값 다 뽑기
        keyValueList = list(gameMapInfo.items())
        print(f"gameMapKeyList: {gameMapKeyList}")
        print(f"gameMapValueList: {gameMapValueList}")
        print(f"keyValueList: {keyValueList}")


