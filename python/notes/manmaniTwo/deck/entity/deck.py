import random


class Deck:
    __cardMap = {}

    def __init__(self):
        shuffledNumberList = random.sample(range(1, 12), 11)
        self.__cardMap = { cardNumber: False for cardNumber in shuffledNumberList }

    def getCardMap(self):
        return self.__cardMap
