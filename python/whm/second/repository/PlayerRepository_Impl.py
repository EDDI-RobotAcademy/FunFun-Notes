from Player.PlayerRepository import PlayerRepository
#인터페이스를 구현하기 위한 구현체
#상징적인거 구현하는 부분
#인터페이스를 구현할 때 보편적으로 Impl
class PlayerRepositoryImpl(PlayerRepository):
    #여러 객체가 불필요하게 메모리를 낭비하며 같은 작업을 반복할 필요가 없다
    __instance=None
    #진짜 생성자
    #결론적으로 singleton(싱글톤) 생성
    def __new__(cls):
        #__new__ 내부에서 cls는 class 자체를 의미합니다.
        #즉 class 내부의 __instance를 보겠다는 뜻
        #이 인스턴스의 내용이 없으면
        #아래와 같이 super().__nwe__(cls)를 통해 만든다는 뜻
        #super().__nwe__(cls)는
        #우선 싱글톤 객체를 만들기 위한 목적으로 사용한다고 기억
        if cls.__instance is None:
            cls.__instance=super().__new__(cls)
        return cls.__instance

    @classmethod
    def getInstane(cls):
        if cls.__instance is None:
            cls.__instance = cls()
            # 이 부분이 실질적으로 __new__이 호출됨
        return cls.__instance

    def Sign(self):
        self.name=input("Insert your name: ")
        return self.name

