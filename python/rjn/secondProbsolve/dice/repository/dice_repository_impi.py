from dice.repository.dice_repository import ABC, abstractmethod, DiceRepository

#인터페이스를 구현하기 위한 구현체입니다.
#앞서 R키를 얘기했는데
#이 궁극기를 구현하는 부분이라고 생각하면 되겠습니다.

# 인터페이스를 구현할 때는 보편적으로 Impl ㅋ워드를 붙입니다.
# Implementation을 의미합니다.
# 그리고 인터페이스의 대상을 '소괄호)' 내부에 집어넣습니다.
# 그러므로 DiceRepository<< 가 안으로 들어감
class DiceRepositoryImpl(DiceRepository) :
    # 이제 논하였듯이 이 인스턴스가 여러개 만들어질 필욕 없습니다
    # 여러 객체가 불필요하게 메모리를 낭비하며 같은 작업을 반복할 필요가 없습니다.
    __interface = None

    #이녀석이 찐 생성자
    #결론적으로 Singleton(싱글콘) 생성 :
    def __new__(cls):
        # __new__ 내부에서 cls는 class 자체를 의미합니다.
        # 즉 class 내부의 __interface를 보겠다는 뜻이고
        # 이 인스턴스의 내용이 없다면
        # 아래와 같이 super().__new(cls)를 통해 만든다는 ㄸㅅ입니다.
        #super().__new(cls)는 우선 그냥 싱글톤 객체를 만들기 위한 목적으로 사용한다고 기억에 박아넣습니다.
        if  cls.__interface is None :
            cls.__interface = super().__new__(cls)

            return cls.__interface


    @classmethod
    def getInstance(cls):

         if cls.__interface is None:

            cls.__interface = cls()
         return cls.__interface

    def rollDice(self):
        pass