class Player:

    def __init__(self):
        self.__name = "Kim"
        self.__age = "20"

    def __str__(self):
        return f"Player:{self.__name, self.__age}"