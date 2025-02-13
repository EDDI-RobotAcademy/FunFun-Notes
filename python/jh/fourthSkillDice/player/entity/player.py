class Player:
    __counter = 1 #  Player가 호출되어 객체를 만들때마다 자동으로 +1씩 더해진다

    def __init__(self, playerName):
        self.__playerName = playerName
        self.__id = Player.__counter
        self.__diceIdList = []
        Player.__counter += 1

    def __str__(self):
        return f"Player(name: {self.__playerName}, diceId: {self.__diceIdList})"

    def getId(self):
        return self.__id

    def addDiceId(self, diceId):
        self.__diceIdList.append(diceId)

    def getDiceIdList(self):
        return self.__diceIdList

# Player
# CashItem
# Order -> Player, CashItem X
#       -> Player[3], CashItem[245]
