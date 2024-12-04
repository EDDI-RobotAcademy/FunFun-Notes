
class Player:
    __counter = 1

    def __init__(self, playerName):
        self.__playerName = playerName
        self.__id = Player.__counter
        Player.__counter += 1

    def __str__(self):
        return f"Player:{self.__playerName}"

    def getId(self):
        return self.__id


    # id 로 player 식별