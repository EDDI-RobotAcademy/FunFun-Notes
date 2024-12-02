from django.db import models


class Dice(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()

    def __str__(self):
        return f"주사위 id: {self.id}, 눈금: {self.number}"

    def get_id(self):
        return self.id

    def get_number(self):
        return self.number

    class Meta:
        db_table = "dice"
