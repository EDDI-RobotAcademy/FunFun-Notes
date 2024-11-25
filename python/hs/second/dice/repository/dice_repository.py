from abc import ABC, abstractmethod
#ABC ABstrack Class 라는 뜻을 가지고 있음
#즉 DiceRepository(ABC)는  '추상화 클래스' 라는 뜻을 가짐
#'추상화 클래스'는 인터페이스

class DiceRepository(ABC):
    @abstractmethod
    def rollDice(self):
        pass
