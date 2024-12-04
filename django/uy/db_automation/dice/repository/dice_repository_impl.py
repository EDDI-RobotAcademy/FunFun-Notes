import random

from django.forms import model_to_dict

from db_automation.dice.entity.dice import Dice
from db_automation.dice.repository.dice_repository import DiceRepository

# DiceRepositoryImpl은 Django 기반 프로젝트에서 주사위 데이터와 관련된 데이터베이스 작업 (저장, 조회 등)을 수행하는 클래스를 정의한 것
class DiceRepositoryImpl(DiceRepository):
    __instance = None

    MIN = 1
    MAX = 6

    def __new__(cls):

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance
    # 싱글톤 패턴을 사용하여 인스턴스 하나만 생성. 효율적인 데이터 관리가 가능해짐

    def create(self):
        # 주사위 데이터를 생성하고 데이터베이스에 저장까지 함
        randomNumber = random.randint(self.MIN, self.MAX) # 1-6 사이에 랜덤 수
        dice = Dice(number=randomNumber)
        # dice라는 Dice객체를 생성하고,
        dice.save()   # db에 저장 (1줄로 완료)

        # return dice
        return model_to_dict(dice)   # db는 딕셔너리 형태로 저장함. model_to_dict()으로 딕셔너리로 저장하게 함


    def findById(self, id):
        # 주사위 id값을 보고서 이 주사위 객체를 찾기 위해서: 낱개 찾기
        # 특정 주사위 데이터를 id로 조회
        return Dice.objects.get(id=id)
        # Dice.objects.get(id=id)로 id에 해당하는 주사위 데이터를 db에서 가져오고 반환까지 함.


    def findAll(self):
        # db에 저장된 모든 주사위 데이터를 조회
        return Dice.objects.all()  # 전부 찾기