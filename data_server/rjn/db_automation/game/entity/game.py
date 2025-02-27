from django.db import models

from game.entity.game_state import GameState


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=255, choices=[(state.name, state.value) for state in GameState])
    playerCount = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Game {self.id}: (state: {self.state})"

    class Meta:
        db_table = 'game'
        app_label = 'game'

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state
