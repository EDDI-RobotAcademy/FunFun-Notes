from django.db import models

from game.entity.game import Game
from player.entity.player import Player


class GameWinnerInfo(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.OneToOneField(Game, on_delete=models.CASCADE, related_name="winner_info")
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="winning_games")

    def __str__(self):
        return f"Game {self.game.id} - Winner: Player {self.player.nickname}"

    class Meta:
        db_table = 'game_winner_info'
        app_label = 'game'

    def getPlayer(self):
        return self.player
