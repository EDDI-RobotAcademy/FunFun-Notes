class Game:
    #HashMap(Dictionary) 생성은 아래와 같이 '중괄호' 줄 표기하여 생성 가능
    #key와 value 형태로 구성되며 key값을 주면 value가 나오게 된다
    __playerDicegameMap={}

    def __init__(self, playerCount):
        self.__playerCount=playerCount

    def getPlayerCount(self):
        return self.__playerCount

    def getPlayerDicegameMap(self):
        return self.__playerDicegameMap

    def setplayerIndexDiceGameMap(self,playerIndexList,diceIdList):
        self.__playerDicegameMap={index:[diceId] for index, dieceId in zip(playerIndexList,diceIdList)}
        print(f"self.__playerDiceGameMap:{self.__playerDicegameMap}")
        #zip의 경우엔 각각의 리스트를 하나로 묶어서 처리할 때 아래와 같은 형태로 사용

    def updatePlayerIndexListMap(self,playerIndexList,diceIdList):
        for index, diceId in zip(playerIndexList,diceIdList):
            if index in self.__playerDicegameMap:
                self.__playerDicegameMap[index].append(diceId)
                continue

            self.__playerDicegameMap[index]=[diceId]

        print(f"self.__playerDicegameMap: {self.__playerDicegameMap}")

    def deleteTargetPlayerId(self,targetPlayerId):
        if targetPlayerId in self.__playerDicegameMap:
            #map에서 특정 쌍 제거
            #정확히는 targetPLayerId를 key로 사용하는 정보를 완전제거
            del self.__playerDicegameMap[targetPlayerId]
        print(f"저격 이후 self.__playerDiceGameMap:{self.__playerDicegameMap}")