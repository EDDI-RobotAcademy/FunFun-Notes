class Game:
    __playerDiceGameMap = {}

    def __init__(self, playerCount):
        self.__playerCount = playerCount

    def getPlayerCount(self):
        return self.__playerCount

    def getPlayerDiceGameMap(self):
        return self.__playerDiceGameMap

    def setPlayerIndexListToMap(self, playerIndexList, diceIdList):
        self.__playerDiceGameMap = { index: [diceId] for index, diceId in zip(playerIndexList, diceIdList) }
        print(f"self.__playerDiceGameMap: {self.__playerDiceGameMap}")

    def updatePlayerIndexListToMap(self, playerIndexList, diceIdList):
        for index, diceId in zip(playerIndexList, diceIdList):
            if index in self.__playerDiceGameMap:
                self.__playerDiceGameMap[index].append(diceId)
                continue

            self.__playerDiceGameMap[index] = [diceId]

        print(f"self.__playerDiceGameMap: {self.__playerDiceGameMap}")
