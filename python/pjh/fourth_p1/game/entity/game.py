class Game:

    __gameMap = {}

    def __init__(self, playerList, eachPlayerDiceList):

        for player, eachPlayerDice in zip(playerList, eachPlayerDiceList):
            # key 로 player를 선택하고 value로 eachPlayerDice를 선택
            self.__gameMap[player] = eachPlayerDice


    def getGameMap(self):
        return self.__gameMap
