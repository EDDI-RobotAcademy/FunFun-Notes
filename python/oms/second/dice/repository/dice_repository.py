from abc import ABC, abstractmethod

'''
* ABC
    python 의 ABC 클래스는 Base 클래스를 상속받는 파생클래스가 
    반드시 Base 클래스의 메서드를 명시적으로 선언해서 구현하도록 강제하는 추상화 클래스 기능이다.

        OOP 의 가장 강력한 기능 중 하나인 상속(Inheritance)은 클래스의 재사용성을 높임으로서, 
        코드의 반복에 따른 유지 보수 비용을 낮추는데 큰 역할을 하였다.
        이러한 상속의 개념과 함께 OOP 의 가장 중요한 특징 중 하나가 바로 다형성(Polymorphism) 이다.
'''
class DiceRepository(ABC):
    @abstractmethod
    def rollDice(self):
        pass