class Game:

    __gameMap = {}

    def __init__(self, playerList, eachPlayerDiceList):
        for player, eachPlayerDice in zip(playerList, eachPlayerDiceList):
            self.__gameMap[player] = eachPlayerDice

       #  print(f"self.gameMap: {self.__gameMap}")

    def getGameMap(self):
        return self.__gameMap