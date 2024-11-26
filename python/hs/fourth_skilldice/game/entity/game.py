class Game:
    __gameMap = {}

    def __init__(self, playerCount):
        self.__playerCount = playerCount

    def getPlayerCount(self):
        return self.__playerCount

    def getGameMap(self):
        return self.__gameMap
