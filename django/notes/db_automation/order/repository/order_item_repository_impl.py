from order.entity.order_items import OrderItems
from order.repository.order_item_repository import OrderItemRepository


class OrderItemRepositoryImpl(OrderItemRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def bulkCreate(self, orderItemList):
        for orderItem in orderItemList:
            if not orderItem.order:
                raise Exception(f"Order item with ID {orderItem.id} has no associated order.")
            print(
                f"Order ID: {orderItem.order.id}, Game Software: {orderItem.game_software.id}, Quantity: {orderItem.quantity}, Price: {orderItem.price}")

        OrderItems.objects.bulk_create(orderItemList)
