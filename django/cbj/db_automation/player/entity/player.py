from django.db import models


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"id: {self.id}, nickname: {self.nickname}"

    def getId(self):
        return self.id

    def getNickname(self):
        return self.nickname

    class Meta:
        db_table = 'player'
