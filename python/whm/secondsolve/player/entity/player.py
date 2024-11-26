class Player():
    __counter=1


    def __init__(self, name):
        self.__name = name
        self.__id=Player.__counter
        self.__diceIdList = []
        Player.__counter+=1
        #name으로 값 받기

    def __str__(self):
        return f"Player{self.__id}(name: {self.__name},diceId: {self.__diceIdList})"
    #self.name값 출력

    def getName(self):
        return self.__name

    # self.name값 출력
    def getId(self):
        return self.__id

    def addDiceId(self,diceId):
        self.__diceIdList.append(diceId)