from django.db import models

from game.entity.game import Game
from player.entity.player import Player


class GamePlayerInfo(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="players")
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="games")

    def __str__(self):
        return f"Game {self.game.id} - Player {self.player.nickname}"

    class Meta:
        db_table = 'game_player_info'
        app_label = 'game'
        unique_together = ('game', 'player')

    def getPlayer(self):
        return self.player
