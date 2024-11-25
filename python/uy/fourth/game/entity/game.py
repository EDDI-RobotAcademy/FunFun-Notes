class Game:
    gameMap = {}

    def __init__(self, playerList, eachPlayerDiceList):
        # 플레이어 리스트, 각 플레이어 주사위 결과 리스트
        for player, eachPlayerDice in zip(playerList, eachPlayerDiceList):
            # Eg) Kim, 5
            self.gameMap[player] = eachPlayerDice
            # gameMap[Kim] = 5

        print(f"self.gameMap: {self.gameMap}")
