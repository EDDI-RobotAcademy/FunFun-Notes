from dice.entity.dice_kinds import DiceKinds
from dice.entity.dice_skill import DiceSkill
from dice.repository.dice_repository_impl import DiceRepositoryImpl
from game.repository.game_repository_impl import GameRepositoryImpl
from game.service.game_service import GameService
from player.repository.player_repository_impl import PlayerRepositoryImpl

import random


class GameServiceImpl(GameService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            # Service Layer에서 Repository Layer를 연결하는 방법
            cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()
            cls.__instance.__playerRepository = PlayerRepositoryImpl.getInstance()
            cls.__instance.__diceRepository = DiceRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def __createGamePlayer(self):
        gamePlayerCount = self.__gameRepository.getGamePlayerCount()

        for _ in range(gamePlayerCount):
            self.__playerRepository.createName()

    def startDiceGame(self, playerCount):
        print("startDiceGame() called!")
        self.__gameRepository.create(playerCount)
        self.__createGamePlayer()


    # def startDiceGame(self):
    #     print("startDiceGame() called!")
    #     self.__gameRepository.create()

    #     self.__createGamePlayer()

    def printCurrentStatus(self):
        game = self.__gameRepository.getGame()
        playerDiceGameMap = game.getPlayerDiceGameMap()
        playerDiceNumberList = []

        for playerId, diceIdList in playerDiceGameMap.items():
            player = self.__playerRepository.findById(playerId)
            for diceId in diceIdList:
                dice = self.__diceRepository.findById(diceId)
                playerDiceNumberList.append(dice.getDiceNumber())

            print(f"플레이어 정보: {player}, 주사위 눈금 리스트: {playerDiceNumberList}")
            playerDiceNumberList.clear()




    # def rollFirstDice(self):
    #     gamePlayerCount = self.__gameRepository.getGamePlayerCount()
    #     playerIndexList = []
    #     diceIdList = []

    #     # 실제 정말 사용자 숫자만큼 반복을 함 (3명이라 가정)
    #     # 위 가정의 경우 0, 1, 2로 playerIndex가 설정됨
    #     for playerIndex in range(gamePlayerCount):
    #         print(f"playerIndex: {playerIndex}")
    #         # 기존에는 단순히 굴리기만 했음
    #         # 혹은 굴리고 Dice 객체 자체를 리턴했음
    #         # 그러나 Player가 어떤 Dice 객체를 소유하고 있는지 판단할 필요가 생겼음
    #         # 그러므로 rollDice() 이후 생성된 주사위의 고유한 번호(id)를 리턴시켰음
    #         diceId = self.__diceRepository.rollDice()
    #         diceIdList.append(diceId)
    #         # 위의 인덱스는 0부터 시작하지만 Entity 구성의 id가 1부터 시작함
    #         # 그러므로 발생한 이격을 조정하기 위해 +1을 해서 검색하고 있음
    #         # findById()를 통해 검색된 Player 객체를 획득
    #         indexedPlayer = self.__playerRepository.findById(playerIndex + 1)
    #         print(f"indexedPlayer: {indexedPlayer}")

    #         playerIndexList.append(playerIndex + 1)

    #         # Player 엔티티에 setDiceId를 구현하여 획득한 주사위의 번호를 설정함
    #         # 고로 특정 Player가 특정 Dice의 소유권을 확보하게 되었음
    #         indexedPlayer.addDiceId(diceId)

    #     for player in self.__playerRepository.acquirePlayerList():
    #         print(f"{player}")

    #     self.__gameRepository.setPlayerIndexListToMap(playerIndexList, diceIdList)
    
    
    
    def rollFirstDice(self):
        print("첫 번째 주사위를 굴립니다.")
        players = self.__playerRepository.acquirePlayerList()

        for player in players:
            diceId = self.__diceRepository.rollDice()
            if diceId is None:
                print(f"Error: 주사위를 생성하지 못했습니다. Player {player.getId()} 건너뜁니다.")
                continue

            player.addDiceId(diceId)
            diceValue = self.__diceRepository.findById(diceId).getDiceNumber()
            self.__gameRepository.getGame().getPlayerDiceGameMap()[player.getId()].append(diceId)

            print(f"Player {player.getId()} ({player.getName()})의 첫 번째 주사위 결과: {diceValue}")

    
    

    def rollSecondDice(self):
        print("두 번째 주사위를 굴립니다.")
        # 디버깅: 각 플레이어의 주사위 상태 확인
        players = self.__playerRepository.acquirePlayerList()
        for player in players:
            print(f"Player {player.getId()}의 주사위 리스트: {player.getDiceIdList()}")

        appliedPlayers = self.__checkSkillAppliedPlayerIndexList()

        for player in appliedPlayers:
            diceId = self.__diceRepository.rollDice()
            player.addDiceId(diceId)
            diceValue = self.__diceRepository.findById(diceId).getDiceNumber()
            self.__gameRepository.getGame().getPlayerDiceGameMap()[player.getId()].append(diceId)

            print(f"Player {player.getId()} ({player.getName()})의 두 번째 주사위 결과: {diceValue}")



    def __checkSkillAppliedPlayerIndexList(self):
        gamePlayerCount = self.__gameRepository.getGamePlayerCount()
        skillAppliedPlayerList = []

        for playerIndex in range(gamePlayerCount):
            indexedPlayer = self.__playerRepository.findById(playerIndex + 1)
            indexedPlayerDiceIdList = indexedPlayer.getDiceIdList()

            # 주사위 ID 리스트가 비어 있는 경우 건너뜀
            if not indexedPlayerDiceIdList:
                print(f"Player {indexedPlayer.getId()}의 주사위 ID 리스트가 비어 있습니다!")
                continue

            indexedPlayerFirstDiceId = indexedPlayerDiceIdList[0]
            indexedPlayerDice = self.__diceRepository.findById(indexedPlayerFirstDiceId)

            if indexedPlayerDice.getDiceNumber() % 2 == 0:
                skillAppliedPlayerList.append(indexedPlayer)

        return skillAppliedPlayerList
        

    def __steelScore(self, playerId):
        game = self.__gameRepository.getGame()
        playerDiceGameMap = game.getPlayerDiceGameMap()

        print(f"현재 상태 :", playerDiceGameMap)

        # 스킬 적용 전 점수 출력
        print("스킬 적용 전 점수 상태:")
        for targetId, diceList in playerDiceGameMap.items():
            totalScore = sum(self.__diceRepository.findById(diceId).getDiceNumber() for diceId in diceList)
            print(f"Player {targetId}: {totalScore} 점")

        # 상대 점수에서 2점씩 빼앗고, 자기 점수에 더함
        for targetId, diceList in playerDiceGameMap.items():
            if targetId == playerId:
                continue  # 자기 자신은 점수 차감 제외

            # 상대 점수에서 2점 차감
            for diceId in diceList:
                dice = self.__diceRepository.findById(diceId)
                currentDiceValue = dice.getDiceNumber()
                newDiceValue = max(0, currentDiceValue - 2)
                dice.setDiceNumber(newDiceValue)

        # 자기 자신에게 2점 추가
        playerDiceList = playerDiceGameMap[playerId]
        if playerDiceList:
            firstDice = self.__diceRepository.findById(playerDiceList[0])
            firstDice.setDiceNumber(firstDice.getDiceNumber() + 2)

        # 스킬 적용 후 점수 출력
        print("스킬 적용 후 점수 상태:")
        for targetId, diceList in playerDiceGameMap.items():
            totalScore = sum(self.__diceRepository.findById(diceId).getDiceNumber() for diceId in diceList)
            print(f"Player {targetId}: {totalScore} 점")

    def __deathShot(self, playerId):
        targetPlayerId = int(input("저격할 상대의 ID를 입력하세요: "))
        self.__gameRepository.deletePlayer(targetPlayerId)
        print(f"Player {targetPlayerId} 제거됨")


    # def __steelScore(self, playerIndex):
    #     game = self.__gameRepository.getGame()
    #     playerDiceGameMap = game.getPlayerDiceGameMap()

    #     for playerId, diceIdList in playerDiceGameMap.items():
    #         if playerId == playerIndex + 1:
    #             firstDiceId = diceIdList[0]
    #             firstDice = self.__diceRepository.findById(firstDiceId)

    #             if firstDice:
    #                 gamePlayerCount = self.__gameRepository.getGamePlayerCount()
    #                 diceNumber = firstDice.getDiceNumber()
    #                 firstDice.setDiceNumber(diceNumber + 2 * (gamePlayerCount - 1))

    #             continue

    #         firstDiceId = diceIdList[0]
    #         firstDice = self.__diceRepository.findById(firstDiceId)

    #         if firstDice:
    #             diceNumber = firstDice.getDiceNumber()
    #             firstDice.setDiceNumber(diceNumber - 2)

    # def __deathShot(self):
    #     game = self.__gameRepository.getGame()
    #     playerDiceGameMap = game.getPlayerDiceGameMap()

    #     playerDiceSum = {}

    #     for playerId, diceIdList in playerDiceGameMap.items():
    #         diceSum = 0

    #         for diceId in diceIdList:
    #             dice = self.__diceRepository.findById(diceId)

    #             if dice:
    #                 diceSum += dice.getDiceNumber()

    #         playerDiceSum[playerId] = diceSum

    #     for playerId, diceSum in playerDiceSum.items():
    #         print(f"플레이어 {playerId}의 누산 점수: {diceSum}")

    #     deathShotTargetPlayerId = int(input('누구를 저격하시겠습니까? '))
    #     self.__gameRepository.deletePlayer(deathShotTargetPlayerId)

    def __applySkill(self, playerIndex, secondDice):
        secondDiceNumber = secondDice.getDiceNumber()
        print(f"secondDiceNumber: {secondDiceNumber}")

        if secondDiceNumber == DiceSkill.STEEL_SCORE.value:
            self.__steelScore(playerIndex)

        if secondDiceNumber == DiceSkill.DEATH_SHOT.value:
            self.__deathShot()

    def applySkill(self):
        print("스킬 주사위를 굴립니다")

        players = self.__playerRepository.acquirePlayerList()
        
        for player in players:
            diceIdList = player.getDiceIdList()
            
            if len(diceIdList) < 2:
                print(f"Player {player.getId()} ({player.getName()})는 두번째 주사위를 굴리지 않습니다")
                continue

            secondDiceId = diceIdList[1]
            secondDiceValue = self.__diceRepository.findById(secondDiceId).getDiceNumber()
            print(f"Player {player.getId()} ({player.getName()}) 스킬 주사위 결과: {secondDiceValue}")

            if secondDiceValue == DiceSkill.STEEL_SCORE.value:
                print(f"STEEL SCORE 발동! 모든 상대에게서 2점을 빼앗습니다")
                self.__steelScore(player.getId())
            elif secondDiceValue == DiceSkill.DEATH_SHOT.value:
                print(f"DEATH SHOT 발동! 상대방 한명을 저격합니다")
                self.__deathShot(player.getId())
            else:
                print("스킬 발동 없음")


    # def applySkill(self):
    #     gamePlayerCount = self.__gameRepository.getGamePlayerCount()

    #     for playerIndex in range(gamePlayerCount):
    #         indexedPlayer = self.__playerRepository.findById(playerIndex + 1)
    #         indexedPlayerDiceIdList = indexedPlayer.getDiceIdList()
    #         indexedPlayerDiceIdListLength = len(indexedPlayerDiceIdList)

    #         if indexedPlayerDiceIdListLength < 2:
    #             continue

    #         indexedPlayerSecondDiceId = indexedPlayerDiceIdList[1]
    #         secondDice = self.__diceRepository.findById(indexedPlayerSecondDiceId)

    #         self.__applySkill(playerIndex, secondDice)

    def checkWinner(self):
        print("최종 점수를 계산합니다.")
        game = self.__gameRepository.getGame()
        playerDiceGameMap = game.getPlayerDiceGameMap()

        if not playerDiceGameMap or all(not diceList for diceList in playerDiceGameMap.values()):
            print("playerDiceGameMap이 비어 있습니다. 승자가 없습니다!")
            return

        playerScores = {}
        for playerId, diceList in playerDiceGameMap.items():
            totalScore = 0
            for diceId in diceList:
                dice = self.__diceRepository.findById(diceId)
                if dice is None:
                    print(f"Player {playerId}의 주사위 ID {diceId}가 유효하지 않습니다!")
                    continue
                totalScore += dice.getDiceNumber()
            playerScores[playerId] = totalScore

        if not playerScores:
            print("모든 플레이어가 제거되었습니다. 승자가 없습니다!")
            return

        maxScore = max(playerScores.values())
        winners = [playerId for playerId, score in playerScores.items() if score == maxScore]

        if len(winners) == 1:
            winnerPlayer = self.__playerRepository.findById(winners[0])
            print(f"우승자: Player {winners[0]} ({winnerPlayer.getName()})")
        else:
            print("무승부입니다!")
            for playerId in winners:
                player = self.__playerRepository.findById(playerId)
                print(f"Player {player.getId()} ({player.getName()})도 {maxScore} 점으로 동점입니다!")

