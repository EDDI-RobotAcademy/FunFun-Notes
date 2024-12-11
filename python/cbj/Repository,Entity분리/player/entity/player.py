class Player:

    def __init__(self, nickname):
        self.__nickname = nickname

    def __str__(self):
        return f"Player: {self.__nickname}"

    def getPlyaerNickname(self):
        return self.__nickname