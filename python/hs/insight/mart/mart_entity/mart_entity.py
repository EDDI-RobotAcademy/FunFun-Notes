class Mart:
    def __init__(self):
        self.fruitMap = {}

    def addFruit(self, fruitName, amount):
        """마트에 과일 추가"""
        self.fruitMap[fruitName] = amount

    def getFruitMap(self):
        return self.fruitMap

