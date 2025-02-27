from rest_framework import serializers

from fruit_mart.order.entity.order import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','customer' ,'number']