from abc import ABC, abstractmethod

class DiceService(ABC):

    @abstractmethod
    def rollDice(self):
        pass

    @abstractmethod
    def findDice(self, requestDiceId):
        pass

    @abstractmethod
    def findEveryDice(self):
        pass


    # Service는 비즈니스 로직 처리를 위해 존재
    #컨트롤러(뷰)와 데이터베이스(모델) 간의 중간 계층 역할이며, 트롤러와 데이터베이스 간의 의존성을 줄임
    # 여러 리포지토리 (repository)또는 모델(entity)를 조합하여 동작함.