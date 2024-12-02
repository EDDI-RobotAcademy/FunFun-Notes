class Mart:
    fruitMap={}

    def addFruit(self,fruitName,fruitAmaount):
        self.fruitMap[fruitName]=fruitAmaount

    def getFruitMap(self):
        return self.fruitMap

