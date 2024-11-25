from dice.repository.dice_repository import DiceRepository
# 인터페이스를 구현하기 위한 구현체 입니다.
# 앞서 R키(국극기)를 얘기했는데
# 이 궁국기를 구현하는 부분이라 생각하면 되겠습니다.

#인터페이스를 구현할 때는 보편적으로 Impl 키워드를 붙입니다.
#Implementation을 의미합니다.
#그리고 인터페이스인 대상을 '소괄호()' 내부에 집어 넣습니다.
#그러므로 DiceRepositoryIn=ml(DiceRepository) <- 이와 같은 문법이 만들어집니다.

class DiceRepositoryImpl(DiceRepository):
    #여러 객체가 불필요하게 메모리를 낭비하여 같은 작업을 반복할 필요가 없습니다.

    __instance = None

    #요 녀석이 사실 찐 생성자
    def __new__(cls):
        #__new__내부에서 cls는 class 자체를 의미합니다.
        # 즉 class 내부의 __instance를 보겠다는 뜻이고
        # 이 인스턴스의 내용이 없다면
        #아래와 같이 super().__new__(cls)를 통해 만든다는 뜻입니다.
        #super().__new__(cls)는
        #우선 싱글톤 객체를 만들기 위한 목적으로 사용한다고 기억에 박아 넣읍시다.
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            #이 부분에서 실질적으로 __new__ 이 호출됨
            cls.__instance = cls()
        return cls.__instance


    def rollDice(self):
        pass