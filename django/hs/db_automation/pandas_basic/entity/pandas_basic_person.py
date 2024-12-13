from django.db import models


class PandasBasicPerson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    def __str__(self):
        return f"PandasBasicPerson id: {self.id}, 이름: {self.name}, 나이: {self.age}"

    class Meta:
        db_table = "pandas_basic_person"
