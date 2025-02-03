class FruitMart:

    __fruitCountMap = {'apple' : 3, 'orange' : 5}

    def __init__(self, fruitKind, fruitCount):
        self.__fruitKind = fruitKind
        self.__fruitCount = fruitCount
        fruit = self.__fruitKind
        count = self.__fruitCount

        self.__fruitCountMap = {fruit : count for fruit, count in zip(fruit, count)}



    def getFruitCountMap(self):
        return self.__fruitCountMap

    def updateFruitCountMap(self, fruit, count):
        self.__fruitCountMap[fruit] = count