class Player:
    __counter = 1
    __diceId = None

    def __init__(self, playerName):
        self.__playerName = playerName
        self.__id = Player.__counter
        Player.__counter += 1

    def __str__(self):
        return f"Player(name: {self.__playerName}, diceId: {self.__diceId})"

    def getId(self):
        return self.__id

    def setDiceId(self, diceId):
        self.__diceId = diceId

# Player
# CashItem
# Order -> Player, CashItem X
#       -> Player[3], CashItem[245]
