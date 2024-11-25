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

        for player, dice in gameMapInfo.items():
            print(f"{player},dice: {dice.getDiceNumber()}")

        winner = max(gameMapInfo, key=lambda player: gameMapInfo[player].getDiceNumber())
        # map에서 각각의 key, value 쌍을 순회하면서 아래의 if 조건에 만족하는 정보만 추려냄.

        maxPlayerList = [player for player, dice in gameMapInfo.items()
                         if dice.getDiceNumber() == gameMapInfo[winner].getDiceNumber()]

        maxPlayerCount = len(maxPlayerList)
        if maxPlayerCount > 1:
            print("무승부입니다.")
            return

        print(f"winner: {winner}")






