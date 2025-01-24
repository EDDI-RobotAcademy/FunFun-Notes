class Dice:

    def __init__(self, diceNumber):
        self.__diceNumber = diceNumber

    def __str__(self):
        return f"Dice Number: {self.__diceNumber}"

    def getDiceNumber(self):
        return self.__diceNumber
