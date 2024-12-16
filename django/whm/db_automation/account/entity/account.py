from django.db import models


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=32)

    class Meta:
        db_table = "account"