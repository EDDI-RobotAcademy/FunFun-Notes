class Dice:

    def __init__(self, diceNum):
        self.__num = diceNum

    def getDiceNum(self):
        return self.__num

    def __str__(self):
        return f"dice number: {self.__num}"

