
class Player:

    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return f"Player:{self.__name}"