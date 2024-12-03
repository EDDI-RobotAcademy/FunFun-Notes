from django.db import models

from game.entity.game_state import GameState


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    winnerId = models.IntegerField(null=True, blank=True)
    loserId = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"Game {self.id}: (winnerId: {self.winnerId}, loserId: {self.loserId})"

    class Meta:
        db_table = 'game'
