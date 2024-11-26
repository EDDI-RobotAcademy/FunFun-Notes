from player.repository.player_repository import playerRepository


#인터페이스를 구현하기 위한 구현체입니다.
#앞서 R키(궁극기)를 애기했는데
#이 궁극기를 구현하는 부분이라 생각하면 되겠습니다.

#인터페이스를 구현할 때는 보편적으로 IMPL 키워드를 붙입니다.
#Implementation을 의미합니다.
#그리고 인터페이스인 대상을 '소괄호()' 내부에 집어넣습니다.
#그러므로 DiceRepositoryIMPL(DiceRepository)<-이와 같은 문법이 만들어집니다.
class PlayerRepositoryImpl(PlayerRepository):
    # 어제 논하였듯이 이 인스턴스가 여러 개 만들어질 필요가 없습니다.
    # 왜냐하면 주사위 굴리는 것은 그냥 굴리면 되기 때문입니다
    # 여러 객체가 불필요하게 메모리를 낭비하며 같은 작업을 반복할 필요가 없습니다.

    __instance = None

    #요 녀석이 사실 찐 생성자
    def __new__(cls):
        #__new__내부에서 cls는 class 자체를 의미합니다.
        #즉 class내부의 __instance 를 보겠다는 뜻이고
        #이 인스턴스의 내용이 없다면
        #아래와 같이 super().__new__(cls)를 통해 만든다는 뜻입니다.
        #super().__new__(cls)는
        #우선 싱글톤 객체를 만들기 위한 목적으로 사용한다고 기억에 박아넣읍시다.
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
                #이 부분에서 실질적으로 __new__이 호출됨
            cls.__instance = cls()

            return cls.__instance

    def rollPlayer(self):
        pass