from django.db import models

class Game(models.Model):
    gameId = models.AutoField(primary_key=True)
    number = models.IntegerField()

    def __init__(self,GameCount):
        self.__gameCount=GameCount


    def __str__(self):
        return f"{self.gameId}째 게임, 합:{self.number}"

    def getId(self):
        return self.id

    def getNumber(self):
        return self.number

    #class Meta:
        #db_table=db이름