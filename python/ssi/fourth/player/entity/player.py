class Player:
    __counter = 1

    def __init__(self, playerName):
        self.__playerName = playerName
        self.__id = Player.__counter
        Player.__counter += 1

    def __str__(self):
        return f"Player#{self.__id} (name: {self.__playerName})"
    
    def getID(self):
        return self.__id
    
    def getName(self):
        return self.__playerName