class Player:
    __counter = 1
    def __init__(self, playerName):
        self.__playerName = playerName
        self.__id = Player.__counter
        self.__diceIdList = []
        Player.__counter += 1

    def __str__(self):
        return f"Player(name: {self.__playerName}, diceId:{self.__diceIdList})"

    def getId(self):
        return self.__id

    def addDiceId(self, diceId):
        self.__diceIdList.append(diceId)

    def getDiceIdList(self):
        return self.__diceIdList

