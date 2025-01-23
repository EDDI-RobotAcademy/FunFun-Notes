class PlayerDice:

    def __init__(self, num):
        self.__num = num

    def __str__(self):
        return f"PlayerDice: {self.__num}"

    def getPlayerDiceNum(self):
        return self.__num


