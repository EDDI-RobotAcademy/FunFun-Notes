class Dice:

    def __init__(self, diceNumber):
        self.__number = diceNumber

    def __str__(self):
        return f"dice number: {self.__number}"

    def getDiceNumber(self):
        return self.__number

class SkillDice:
    def __init__(self, skillDiceNumber):
        self.__number = skillDiceNumber
    def __str__(self):
        return f"skill dice number: {self.__number}"

    def getSkillDiceNumber(self):
        return self.__number