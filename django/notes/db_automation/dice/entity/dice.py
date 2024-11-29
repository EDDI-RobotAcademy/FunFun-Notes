from django.db import models


class Dice(models.Model):
    # 앞서 우리가 고유한 유일 숫자값 만들 것
    __id = models.AutoField(primary_key=True)
    # 주사위 눈금은 숫자
    __number = models.IntegerField()

    def __str__(self):
        return f"주사위 id: {self.__id}, 눈금: {self.__number}"

    def getId(self):
        return self.__id

    def getNumber(self):
        return self.__number

    class Meta:
        db_table = "dice"
