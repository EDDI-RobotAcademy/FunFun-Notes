from game.repository.game_repository import GameRepository
from game.entity.game import Game

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
        game = Game(playerNameList, eachPlayerDiceList)  # Game 객체 생성
        self.__gameList.append(game)   # gameList = [game]

    def checkWinner(self):
        game = self.__gameList[0]
        gameMapInfo = game.getGameMap()

        # Dictionary의 key 값 다 뽑기
        gameMapKeyList = gameMapInfo.keys()
        # Dictionary의 value 값 다 뽑기
        gameMapValueList = gameMapInfo.values()
        # Dictionary의 key, value 값 다 뽑기
        keyValueList = list(gameMapInfo.items())
        # key:a , value :2 -> list화 -> [('a', 2), ('b', 3), ('c', 4)]

        print(f"gameMapKeyList: {gameMapKeyList}")
        print(f"gameMapValueList: {gameMapValueList}")
        print(f"keyValueList: {keyValueList}")

        for player,dice in gameMapInfo.items():
            print(f"{player},dice:{dice.getDiceNumber()}")

        winner = max(gameMapInfo, key=lambda player: gameMapInfo[player].getDiceNumber())
        maxPlayerList = [player for player, dice in gameMapInfo.items()
                         if dice.getDiceNumber() == gameMapInfo[winner].getDiceNumber()]
        maxPlayerList = len(maxPlayerList)

        # apply skill
        if maxPlayerList > 1:
            print("무승부 입니다!")
            return

        print(f"winner: {winner}")




        # Alt + Insert : Override 추가
