from abc import ABC, abstractmethod


#ABC는 Abstract Class 라는 뜻을 가지고 있음.
#즉, DiceRepository(ABC)는 '추상화 클래스'라는 뜻을 가짐
# '추상화클래스'는 인터페이스들의집합
#인터페잇란용어가 와닿지않을테니 LOL의 궁극기R이라고 생각하면 됨


class DiceRepository(ABC) :

    #abstractmethod ABC 클래스 내에 인터페이스를 선언 할 경우 사용
    @abstractmethod
    def rollDice(self):
        # 아무것도 하지않음 (pass) : 상징성만 줄 뿐
        pass