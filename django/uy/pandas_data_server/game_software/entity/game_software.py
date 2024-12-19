from django.db import models

# Create your models here.


class GameSoftware(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)

    class Meta:
        db_table = 'game_software'
        app_label = 'game_software'

    def getId(self):
        return self.id

    def getTitle(self):
        return self.title
