import random

from django.forms import model_to_dict

from dice.entity.dice import Dice
from dice.repository.dice_repository import DiceRepository

class DiceRepositoryImpl(DiceRepository):
    __instance=None

    MIN=1
    MAX=6

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance=super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance= cls()

            return cls.__instance

    def create(self):
        randomNumber=random.randint(self.MIN,self.MAX)
        dice=Dice(number=randomNumber)
        dice.save()
        #db에 저장한다

        return model_to_dict(dice)
        #Web Page에서 주고받는 데이터는 전부 json형식을 따름
        #JSON 형식은 기본적으로 key,Value 형태의 Dictionary 구성임
        #그러므로 model to dict는 엔티티를 Dictionary로 변경하여 리턴함을 의미

    def findById(self,id):
        return Dice.objects.get(id=id)

    def findAll(self):
        return Dice.objects.all()

