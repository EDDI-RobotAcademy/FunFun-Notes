class Fruit:
    def __init__(self, fruitName, fruitCount):
        self.__fruitName = fruitName
        self.__fruitCount = fruitCount

    def __str__(self):
        return f"Fruit(name: {self.__fruitName}, fruitCount: {self.__fruitCount}"

    def get_fruit_name(self):
        return self.__fruitName

    def get_fruit_count(self):
        return self.__fruitCount

fruit1 = Fruit("사과", 3)
fruit2 = Fruit("오렌지", 5)
fruit3 = Fruit("배", 0)

fruitList = [fruit1, fruit2, fruit3]

fruitNameList = [fruit.get_fruit_name() for fruit in fruitList]
fruitCountList = [fruit.get_fruit_count() for fruit in fruitList]

for name, count in zip(fruitNameList, fruitCountList):
    print(f"{name}: {count}")
