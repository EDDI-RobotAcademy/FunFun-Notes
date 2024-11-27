from abc import ABC, abstractmethod

class PlayerRepository(ABC):
    # abstractmethod는 ABC클래스 내에 인터페이스를 선언 할 경우 사용
    @abstractmethod
    def createName(self):
        pass