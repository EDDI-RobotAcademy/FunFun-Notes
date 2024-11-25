class Game:
    gameMap = {}

    def __init__(self, playerList, eachPlayerDiceList):
        for player, eachPlayerDice in zip(playerList, eachPlayerDiceList):
            self.gameMap[player] = eachPlayerDice

        print(f"self.gameMap: {self.gameMap}")
