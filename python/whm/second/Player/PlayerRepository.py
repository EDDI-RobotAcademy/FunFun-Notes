from abc import ABC, abstractmethod
# ABC는 ABstract Class라는 뜻
# wmr DisceRepository(ABC)는 '추상화 클래스'라는 뜻
# '추상화 클래스'는 인터페이스들의 집합
# 인터페이스란 상징적인 하나가 누가 쓰냐에 따라 다른것을 나타냄
class PlayerRepository(ABC):
    # abstractmethod는 ABC클래스 내에 인터페이스를 선언 할 경우 사용
    @abstractmethod
    def Sign(self):
    # 아무것도 하지 않음(pass)
        pass