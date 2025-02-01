from game.entity.game import Game
from game.repository.game_repository import GameRepository


class GameRepositoryImpl(GameRepository):

    __instance = None

    __gameList = []

    __gameMapInfo = {}

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
        for game in self.__gameList:
            gameMapInfo = game.getGameMap()
            self.__gameMapInfo.update(gameMapInfo)

        for player, dice in self.__gameMapInfo.items():
            print(f"{player}, dice: {dice}")


        winner = max(self.__gameMapInfo, key=lambda player: self.__gameMapInfo[player].getDiceNumber())
        maxPlayerList = [player for player, dice in self.__gameMapInfo.items()
                         if dice.getDiceNumber() == self.__gameMapInfo[winner].getDiceNumber()]

        maxPlayerCount = len(maxPlayerList)
        if maxPlayerCount > 1:
            print("무승부입니다!")
            return

        print(f"winner: {winner}")


