from django.db import models

from game_software.entity.game_software import GameSoftware


class GameSoftwareDescription(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(GameSoftware, on_delete=models.CASCADE, related_name="prices")
    description = models.TextField()

    class Meta:
        db_table = 'game_software_description'
        app_label = 'game_software'
