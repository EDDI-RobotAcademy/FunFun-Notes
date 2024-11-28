class Account:
    __counter = 1

    def __init__(self, accountId, password):
        self.__accountId = accountId
        self.__password = password
        self.__id = Account.__counter
        Account.__counter += 1

    def getAccountId(self):
        return self.__accountId

    def getPassword(self):
        return self.__password

    def getId(self):
        return self.__id
