import random 

# 클래스 생성
# 클래스 -> 도메인
class dice: 

    MAX=6
    MIN=1

    # __init__() 생성자
    def __init__(self): 
        # __: private 지정
        self.__number=0
    
    def rollDice(self): 
        # self.__number=random.randint(self.MAX, self.MIN)
        self.__number=1
    
    def printResult(self):
        print(f"dice number: {self.__number}")