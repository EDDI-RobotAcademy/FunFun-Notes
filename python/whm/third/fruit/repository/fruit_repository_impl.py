from fruit.repository.fruit_repository import FruitRepository
from fruit.entity.fruit import Fruit

class FruitRepositoryImpl(FruitRepository):
    __instance=None
    #과일종류리스트
    __todayFruit=[]
    #종류별갯수리스트
    __fruitNumber=[]

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance=super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance=cls()

        return cls.__instance
    #싱글톤

    #과일종류 수
    def __fruitNum(self):
        fruitType = int(input("오늘 몇개의 과일이 들어왔습니까?"))
        return fruitType

    #과일종류별 이름과 갯수
    def createFruit(self):
        number=self.__fruitNum()
        for i in range(number):
            fruitName=input("오늘 들어온 과일은 무엇입니까?")
            numbering = int(input("몇개입니까?"))
            self.__todayFruit.append(fruitName)
            self.__fruitNumber.append(numbering)


    # 과일 종류리스트
    def createTodayFruit(self):
        return self.__todayFruit

    # 종류별 갯수리스트
    def createFruitNumber(self):
        return self.__fruitNumber

    def AllList(self):
        for fruit, num in zip(self.__todayFruit,self.__fruitNumber):
            home=Fruit(fruit, num)
            print(home)