from dice.repository.dice_repository import DiceRepository

# 인터페이스를 구현하기 위한 구현체임
# 앞서 얘기한 R키(궁극기)를 구현하는 부분임
# 인터페이스를 구현할 때는 보편적으로 Impl 키워드를 붙임 (Implementation)
#

class DiceRepositoryImpl(DiceRepository):
    # 여러 객체가 불필요하게 메모리를 낭비하며 같은 작업을 반복할 필요가 없음

    # 아래의 __new__ 내부에서 cls는 Class 자체를 의미함
    # 즉, class 내부의 __instance를 보겠다는 뜻이고, 이 인스턴스의 내용이 없다면
    # super().__new__(cls)를 통해 만듦
    # 이 과정은 싱글톤 객체를 만들기 위한 목적으로 사용됨

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            # 이 부분에서 실질적으로 __new__ 가 호출됨
            cls.__instance = cls()

        return cls.__instance

    def rollDice(self):
        pass

