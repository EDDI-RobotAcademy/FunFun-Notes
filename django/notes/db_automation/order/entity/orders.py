from django.db import models

from account.entity.account import Account
from order.entity.order_status import OrderStatus


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='order')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=OrderStatus.choices, default=OrderStatus.PENDING)  # 주문 상태
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 업데이트 시간

    def __str__(self):
        return f"Order {self.id}"

    class Meta:
        db_table = 'orders'
        app_label = 'order'

    def getId(self):
        return self.id
