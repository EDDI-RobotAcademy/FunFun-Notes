from django.db import models
from account.entity.account import Account

class Interview(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="interviews")
    topic = models.CharField(max_length=255)
    yearsOfExperience = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the interview is created

    class Meta:
        db_table = 'interview'
        app_label = 'interview'

    def __str__(self):
        return f"Interview(id={self.id}, account={self.account}, topic={self.topic}, yearsOfExperience={self.yearsOfExperience})"

    def getId(self):
        return self.id

    def getAccount(self):
        return self.account

    def getTopic(self):
        return self.topic

    def getYearsOfExperience(self):
        return self.yearsOfExperience

    def getCreatedAt(self):
        return self.created_at
