class Turn:

    def __init__(self):
        self.__turnCount = 1

    def addTurnCount(self):
        self.__turnCount += 1

    def getTurnCount(self):
        return self.__turnCount
