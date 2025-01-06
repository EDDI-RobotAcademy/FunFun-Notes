from django.db import models

from game_software.entity.game_software import GameSoftware
from order.entity.orders import Order


class OrderItems(models.Model):
    id = models.AutoField(primary_key=True)
    orders = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)  # Order와 연결
    game_software = models.ForeignKey(GameSoftware, related_name="items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item: {self.quantity} x {self.price}"

    class Meta:
        db_table = 'order_items'
        app_label = 'order'