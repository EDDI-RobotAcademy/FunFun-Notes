class Player:

    def __init__(self,playerName):
        self.__playerName = playerName

    def __str__(self):
        return f"Player Name: {self.__playerName}"