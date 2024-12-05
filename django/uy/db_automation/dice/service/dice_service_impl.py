from db_automation.dice.service.dice_service import DiceService
from db_automation.dice.repository.dice_repository_impl import DiceRepositoryImpl


# DiceService를 상속받아 구현.
# **DiceServiceImpl**는 주사위 데이터를 생성, 조회하는 서비스 계층.
class DiceServiceImpl(DiceService):
    __instance = None

    # 데이터 접근 로직(Repository)와 컨트롤러(Controller)간의 중재자 역할을 함.

    def __new__(cls):

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__diceRepository = DiceRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def rollDice(self):
        return self.__diceRepository.create()
    # create(): db에 저장하고 model_to_dict(dice) dice를 딕셔너리 형태로 저장
    # Repository 계층의 create() 메서드를 호출하며, 무작위 주사위 데이터를 생성하고 저장.
    # 반환값: 생성된 주사위 데이터를 JSON형식으로 반환


    def findDice(self, requestDiceId):
        # 특정 주사위 데이터를 id로 조회
        return self.__diceRepository.findById(requestDiceId)
        # Repository 계층의 findById를 호출
        # 입력: requestDiceId (조회할 주사위의 ID).
        # 반환값: 주사위 객체


    def findEveryDice(self):
        # 모든 주사위 데이터를 조회
        return self.__diceRepository.findAll()
        # Repository 계층의 findAll() 메서드 호출
        # 반환값: 모든 주사위 데이터의 리스트 (쿼리셋)

