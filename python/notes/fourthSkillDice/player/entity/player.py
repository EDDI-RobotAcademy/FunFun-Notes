class Player:
    __counter = 1

    def __init__(self, playerName):
        self.__playerName = playerName
        self.__id = Player.__counter
        Player.__counter += 1

    def __str__(self):
        return f"Player(name: {self.__playerName})"

    def getId(self):
        return self.__id

# Player
# CashItem
# Order -> Player, CashItem X
#       -> Player[3], CashItem[245]
