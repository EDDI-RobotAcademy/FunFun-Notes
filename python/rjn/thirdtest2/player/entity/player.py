

class Player :

    def __init__(self, playerName):
        self.__name = playerName

    def __str__(self):
        return f"player 이름 : {self.__name}"