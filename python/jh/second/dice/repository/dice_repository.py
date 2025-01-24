from abc import ABC, abstractmethod

# ABC는 ABstract Class 라는 뜻임
# 즉, DiceRepository(ABC)는 '추상화 클래스'라는 뜻을 가짐
# 추상화 클래스란, 인터페이스의 집합임. 롤의 궁극기라고 생각하면 됨
# 뭔 말이냐면, R키는 궁극기지만, 캐릭터마다 각각 다른 궁극기가 나옴
# 예를 들어, 다양한 주사위가 있는데, 결국 전부 주사위인 것처럼,
# 다양한 기능을 만들 때 정리하기 위해 사용함
class DiceRepository(ABC):

    # abstractmethod는 클래스 내에 인터페이스를 선언할 경우 사용
    @abstractmethod
    def rollDice(self):
        # 아무것도 하지 않을때, pass 씀
        pass