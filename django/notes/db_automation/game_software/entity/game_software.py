from django.db import models

class GameSoftware(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)

    class Meta:
        db_table = 'game_software'
        app_label = 'game_software'
