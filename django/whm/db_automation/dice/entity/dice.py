from django.db import models

from game.entity.game import Game
from player.entity.player import Player


class Dice(models.Model):
    # 앞서 우리가 고유한 유일 숫자값 만들 것
    id = models.AutoField(primary_key=True)
    # 주사위 눈금은 숫자
    number = models.IntegerField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='dice')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='dice')

    def __str__(self):
        return f"주사위 id: {self.id}, 눈금: {self.number}"

    def getId(self):
        return self.id

    def getNumber(self):
        return self.number

    def getPlayer(self):
        return self.player

    def getGame(self):
        return self.game

    class Meta:
        db_table = "dice"
