class Game:
    __playerDiceGameMap = {}   #굳이 새판마다 delete 번거롭게 하기보다 game에서 관리하는게 좀 더 효율적일 가능성?

    def __init__(self, playerCount):
        self.__playerCount = playerCount

    def getPlayerCount(self):
        return self.__playerCount

    def getPlayerDiceGameMap(self):
        return self.__playerDiceGameMap

    def setPlayerIndexListToMap(self, playerIndexList, diceIdList):
        self.__playerDiceGameMap = { index: [diceId] for index, diceId in zip(playerIndexList, diceIdList) }
        print(f"self.__playerDiceGameMap: {self.__playerDiceGameMap}")

    def updatePlayerIndexListToMap(self, playerIndexList, diceIdList):
        for index, diceId in zip(playerIndexList, diceIdList):
            if index in self.__playerDiceGameMap:
                self.__playerDiceGameMap[index].append(diceId)
                continue

            self.__playerDiceGameMap[index] = [diceId]

        print(f"self.__playerDiceGameMap: {self.__playerDiceGameMap}")

    def deleteTargetPlayerId(self, targetPlayerId):
        if targetPlayerId in self.__playerDiceGameMap:
            # Map에서 특정 쌍 완전히 제거
            # 정확히는 targetPlayerId를 key로 사용하는 정보를 완전히 제거함
            del self.__playerDiceGameMap[targetPlayerId]

        print(f"저격 이후 self.__playerDiceGameMap: {self.__playerDiceGameMap}")

