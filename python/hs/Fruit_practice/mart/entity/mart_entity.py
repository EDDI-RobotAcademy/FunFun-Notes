class Mart:
    def __init__(self):
        self.fruitMap = {}


    def addFruit(self, fruitName, addAmount):
        self.fruitMap[fruitName] = addAmount


    def sellFuit(self, fruitName, sellAmount):
        self.fruitMap[fruitName] -= sellAmount

    def getFruitMap(self):
        return self.fruitMap
