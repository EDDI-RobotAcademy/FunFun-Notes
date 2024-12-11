class Fruit:
    fruitNameList = []

    def __init__(self, fruitName, fruitCount):
        self.fruitName = fruitName
        self.fruitCount = fruitCount

        if fruitName not in Fruit.fruitNameList:
            Fruit.fruitNameList.append(fruitName)

    def __str__(self):
        return f"FruitName: {self.fruitName}, FruitCount: {self.fruitCount}"

apple = Fruit("Apple", 3)
orange = Fruit("Orange", 5)
pear = Fruit("Pear", 0)
print(apple)
print(orange)
print(pear)