class Player:

    def __init__(self):
        self.__nickname = "아무개"

    def setNickname(self, nickname):
        self.__nickname = nickname

    def __str__(self):
        return f"Player: {self.__nickname}"
