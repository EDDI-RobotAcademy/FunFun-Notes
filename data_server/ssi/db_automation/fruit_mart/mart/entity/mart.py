from django.db import models

class Mart(models.Model):
    id = models.AutoField(primary_key=True)
    fruit_name = models.CharField(max_length=255)
    fruit_number = models.IntegerField()

    def __str__(self):
        return(
            f"Mart(id={self.id},fruit_name={self.fruit_name},fruit_number={self.fruit_number}"
        )

    class Meta:
        db_table='FruitMart'