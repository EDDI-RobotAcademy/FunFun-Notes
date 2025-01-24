class Player:

    def __init__(self, selectedName):
        self.__name = selectedName

    def __str__(self):
        return f"Player name: {self.__name}"

