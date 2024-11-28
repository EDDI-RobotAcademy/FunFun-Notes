class Game:
    __state = None

    def updateState(self, state):
        self.__state = state

    def getState(self):
        return self.__state
