from abc import ABC, abstractmethod
# 추상화 클래스 생성
class DiceRepository(ABC):
    #인터페이스 생성
    @abstractmethod
    #추상화 클래스 내 인터페이스 생성을 위해 사용

    def rollDice(self):
        pass
    #동작 하지 않는 함수 정의
    @abstractmethod
    def findById(self,diceId):
        pass