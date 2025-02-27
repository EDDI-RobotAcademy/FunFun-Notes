from django.db import models
#from fruit_mart.customer.entity.cumstomer import Customer
from fruit_mart.mart.entity.mart import Mart

class Order(models.Model):
    customerNickName = models.CharField(max_length=255)
    # 소비자 이름 입력받기
    buyNumber=models.IntegerField()
    #구매갯수 입력받기
    fruitType= models.CharField(max_length=255)
    # 구매할 과일종류 입력받기

    def __str__(self):
        return f"{self.customerNickName} - {self.fruitType} ({self.buyNumber})"

    class Meta:
        db_table="order_table"


