from game.entity.game import Game
from game.repository.game_repository import GameRepository


class GameRepositoryImpl(GameRepository):
    __instance = None

    __gameList = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def start(self, playerNameList, eachPlayerDiceList):
        game = Game(playerNameList, eachPlayerDiceList)
        self.__gameList.append(game)

# Firstskill = 숫자 4를 뽑은 플레이어가 상대를 저격하여 제거하는 스킬
    def pickFirstskillUser(self):
        game = self.__gameList[0]
        firstSkillPlayerInfo = game.getGameMap()
        firstSkillPlayerDiceNumber = firstSkillPlayerInfo.values()
        firstskillPlayerName = firstSkillPlayerInfo.keys()
        if firstSkillPlayerDiceNumber == 4:
            print(f"{firstskillPlayerName}님의 스킬이 활성화되었습니다.")
            return firstskillPlayerName
        return None

    def useFirstskill(self):
        firstskillPlayer = self.pickFirstskillUser()
        if firstskillPlayer:
            userInput = input(f"저격할 플레이어를 입력해주세요:")
            print(userInput)


    def checkWinner(self):
        game = self.__gameList[0]
        gameMapInfo = game.getGameMap()

        for player, dice in gameMapInfo.items():
            print(f"{player}, dice: {dice.getDiceNumber()}")


        winner = max(gameMapInfo, key=lambda player: gameMapInfo[player].getDiceNumber())
        maxPlayerList = [player for player, dice in gameMapInfo.items()
                         if dice.getDiceNumber() == gameMapInfo[winner].getDiceNumber()]

        maxPlayerCount = len(maxPlayerList)
        if maxPlayerCount > 1:
            print("무승부입니다!")
            return

        print(f"winner: {winner}")
