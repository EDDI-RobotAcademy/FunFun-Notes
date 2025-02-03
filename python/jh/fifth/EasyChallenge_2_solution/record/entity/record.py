class Record:
    def __init__(self, accountUniqueId, turnCountNumber, isWin):
        self.__accountUniqueId = accountUniqueId
        self.__turnCountNumber = turnCountNumber
        self.__isWin = isWin

    def getAccountUniqueId(self):
        return self.__accountUniqueId

    def getTurnCountNumber(self):
        return self.__turnCountNumber

    def getIsWin(self):
        return self.__isWin
