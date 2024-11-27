import random
#랜덤함수 선언
from dice.entity.dice import Dice
from dice.repository.dice_repository import DiceRepository


class DiceRepositoryImpl(DiceRepository):
    __instance = None
    # instance 생성
    __dicelist=[]
    #빈 리스트 생성, 여기에 주사위 정보 저장
    #즉 이번 케이스는 rolldice()가 구동 될 때마다 누적됨

    MIN = 1
    MAX = 6
    #최대,최소값 상수에 지정

    def __new__(cls):
        #진짜 생성자 생성
        if cls.__instance is None:
            #cls는 자신이 있는 클래스를 본다.
            #즉, DiceRepository내를 본다는 의미
            #cls.__instance는 DiceRepository안의 __instance를 의미
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    #주사위 굴리기 구현
    def rollDice(self):
        diceNumber = random.randint(self.MIN, self.MAX)
        #diecNumber에 랜덤값 대입
        dice = Dice(diceNumber)
        #diec에 Dice클래스에서 diceNumber를 대입한 결과 대입
        self.__dicelist.append(dice)
        #dicelsit에 값 추가
        return dice.getId()
        #dice에서 id값 출력

    def findById(self,diceId):
        #dicelist값 나열
        for dice in self.__dicelist:
            #그중 diceId가 같다면
            if dice.getId()==diceId:
                #결과 출력
                return dice

    #리스트에 굴린결과 출력
    def acquireDiceList(self):
        return self.__dicelist