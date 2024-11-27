from game.repository.game_repository_impl import GameRepositoryImpl
from game.service.game_service import GameService
from dice.repository.dice_repository_impl import DiceRepositoryImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl
from dice.entity.dice_skill import DiceSkill
from dice.entity.dice_kinds import DiceKinds

class GameServiceImpl(GameService):
    __instance = None

    def __new__(cls):
        #진짜 생성자 생성
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            #service layer에서 repository layer를 연결하는 방법
            cls.__instance.__gameRepository=GameRepositoryImpl.getInstance()
            cls.__instance.__playerRepository=PlayerRepositoryImpl.getInstance()
            cls.__instance.__diceRepository=DiceRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance
    #싱글톤 생성
    def __createPlayer(self):
        gamePlayerCount=self.__gameRepository.getGamePlayerCount()
        for i in range(gamePlayerCount):
            self.__playerRepository.createName()

    def startDiceGame(self):
        print("Game Start!")
        self.__gameRepository.create()
        self.__createPlayer()

    def printCurrentStatus(self):
        game=self.__gameRepository.getGame()
        playerDiceGameMap=game.getPlayerDicegameMap()
        playerDiceNumberList=[]

        for playerId,diceIdList in playerDiceGameMap.items():
            player=self.__playerRepository.findId(playerId)
            for diceId in diceIdList:
                dice=self.__diceRepository.findById(diceId)
                playerDiceNumberList.append(dice.getDiceNumber())
            print(f"플레이어 정보:{player},주사위 눈금 리스트:{playerDiceNumberList}")
            playerDiceNumberList.clear()

    def rollFirstDice(self):
        gamePlayerCount=self.__gameRepository.getGamePlayerCount()
        #gamePlayerCount에 플레이어들 인원수를 추가
        playerIndexList=[]
        diceIdList=[]

        #playerindex가 0~플레이어 인원수만큼 가짐
        #player가 어떤 dice객체를 소유하고 있는지 판단필요
        #rollDice()이후 diceId를 리턴
        for index in range(gamePlayerCount):
            diceId = self.__diceRepository.rollDice()
            num=self.__diceRepository.findById(index+1)
            #num에는 dice에서 findById를 통해 그diceId에 해당하는 주사위 값을 가짐
            indexedPlayer=self.__playerRepository.findId(index+1)
            #indexedPlayer에는 findId()로 Id가 1인 플레이어부터  들어간다
            indexedPlayer.addDiceId(diceId)
            playerIndexList.append(diceId)
            #addDiceId()를 통해 플레이어마다 diceId를 획득한다
            print(f"{indexedPlayer},diceNumber:{num}")

        for player in self.__playerRepository.acquireTeam():
            print(f"{player}")

    #짝수가 있는지 판별하는 함수
    def __checkSkillAppliedPlayerList(self):
        gamePlayerCount=self.__gameRepository.getGamePlayerCount()
        skillAppiedPlayerList=[]
        #주사위값이 짝수가 나와 해당되는 플레이어를 넣을 리스트

        for Index in range(gamePlayerCount):
            subPlayer= self.__playerRepository.findId(Index+1)
            subPlayerDiceIdList=subPlayer.getDiceIdList()
            subPlayerFirstId=subPlayerDiceIdList[0]
            #첫번째 diceId만 가져온다
            subPlayerDice=self.__diceRepository.findById(subPlayerFirstId)
            if subPlayerDice.getDiceNumber()%2==0:
                skillAppiedPlayerList.append(Index+1)

        return skillAppiedPlayerList

    def rollSecondDice(self):
        skillAppiedPlayerList=self.__checkSkillAppliedPlayerList()
        skillAppiedPlayerLength=len(skillAppiedPlayerList)
        secondDiceIdList=[]

        for index in range(skillAppiedPlayerLength):
            secondDiceId=self.__diceRepository.rollDice()
            secondDiceIdList.append(secondDiceId)
            #두번째 주사위 돌리기

            skillAppiedPlayerIndex=skillAppiedPlayerList[index]
            skillAppiedPlayer=self.__playerRepository.findId(skillAppiedPlayerIndex)
            skillAppiedPlayer.addDiceId(secondDiceId)
            print(f"skillAppliedPlayer:{skillAppiedPlayer}")

            secondDice=self.__diceRepository.findById(secondDiceId)
            secondDice.setDiceKinds(DiceKinds.SPECIAL)
            print(f"secondDice: {secondDice}")
        self.__gameRepository.updatePlayerIndexListMap(
            skillAppiedPlayerList,secondDiceIdList)

    def __steelScore(self,playerIndex):
        game=self.__gameRepository.getGame()
        playerDiceGameMap=game.getPlayerDicegameMap()

        for playerId,diceIdList in playerDiceGameMap.items():
            if playerId==playerIndex+1:
                firstDiceId=diceIdList[0]
                firstDice=self.__diceRepository.findById(firstDiceId)

                if firstDice:
                    gamePlayerCount=self.__gameRepository.getGamePlayerCount()
                    diceNumber=firstDice.getDiceNumber()
                    firstDice.setDiceNumber(diceNumber+2*(gamePlayerCount-1))

                continue

            firstDiceId=diceIdList[0]
            firstDice=self.__diceRepository.findById(firstDiceId)

            if firstDice:
                diceNumber=firstDice.getDiceNumber()
                firstDice.setDiceNumber(diceNumber-2)


    def __deathshot(self):
        game=self.__gameRepository.getGame()
        playerDiceGameMap=game.getPlayerDicegameMap()

        playerDiceSum={}

        for playerId,diceIdList in playerDiceGameMap.items():
            diceSum=0

            for diceId in diceIdList:
                dice=self.__diceRepository.findById(diceId)

                if dice:
                    diceSum+=dice.getDiceNumber()

            playerDiceSum[playerId]=diceSum

        for playerId, diceSum in playerDiceSum.items():
            print(f"플레이어 {playerId}의 누산 점수: {diceSum}")

        deathShotTargetPlayerId=int(input("누구를 저격하겠습니까?"))
        self.__gameRepository.deleteTargetPlayer(deathShotTargetPlayerId)

    def __applySkill(self,playerIndex,secondDice):
        secondDiceNumber=secondDice.getDiceNumber()
        print(f"secondDieNumber:{secondDiceNumber}")

        if secondDiceNumber==DiceSkill.STEEL_SCORE.value:
            self.__steelScore(playerIndex)

        if secondDiceNumber==DiceSkill.DEATH_SHOT.value:
            self.__deathshot()

    def applySkill(self):
        gamePlayerCount=self.__gameRepository.getGamePlayerCount()

        for playerIndex in range(gamePlayerCount):
            indexPlayer=self.__playerRepository.findId(playerIndex+1)
            indexPlayerDiceIdList=indexPlayer.getDiceIdList()
            indexPlayerDiceIdListLength=len(indexPlayerDiceIdList)

            if indexPlayerDiceIdListLength<2:
                continue
            indexPlayerSecondDiceId=indexPlayerDiceIdList[1]
            secondDice=self.__diceRepository.findById(indexPlayerSecondDiceId)

            self.__applySkill(playerIndex,secondDice)


    def checkWinner(self):
        game = self.__gameRepository.getGame()
        playerDiceGameMap=game.getPlayerDicegameMap()

        playerDiceSum={}

        for playerId,diceIdlist in playerDiceGameMap.items():
            diceSum=0

            for diceId in diceIdlist:
                dice=self.__diceRepository.findById(diceId)

                if dice:
                    diceSum+=dice.getDiceNumber()

            playerDiceSum[playerId]=diceSum

        maxDiceSum=max(playerDiceSum.values())
        maxDicePlayerList=[playerId for playerId,diceSum in playerDiceSum.items()
                           if diceSum==maxDiceSum]

        if len(maxDicePlayerList)>1:
            print("무승부")
            return


        winnerId=maxDicePlayerList[0]
        winner=self.__playerRepository.findId(winnerId)
        print(f"승자:{winner}")