from django.db import models

class Dice(models.Model):
    number=models.IntegerField()

    def __str__(self):
        return f"주사위 id:{self.id},눈금:{self.number}"

    def getId(self):
        return self.id

    #class Meta:
        #db_table=db이름