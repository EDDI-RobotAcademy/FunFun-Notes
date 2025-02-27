from fruit_mart.order.repository.order_repository_impl import OrderRepositoryImpl
from fruit_mart.mart.repository.mart_repository_impl import MartRepositoryImpl

class OrderServiceImpl:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.orderRepository = OrderRepositoryImpl.getInstance()
            cls.__instance.martRepository = MartRepositoryImpl()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def buyFruit(self, customer, fruit, number):
        if not customer or not fruit or not number:
            raise ValueError("All fields are required")
        # Business logic for purchasing fruit
        self.martRepository.decrease_stock(fruit, int(number))
        return self.orderRepository.create(customer, fruit, number)

    def findOrderByCustomer(self, customer_name):
        return self.orderRepository.findByCustomer(customer_name)
    
    def refundOrder(self, order_id, refund_quantity, refund_item):
        try:
            refund_quantity = int(refund_quantity)
        except ValueError:
            raise ValueError("Refund quantity must be a valid integer")

        order = self.orderRepository.findById(order_id)
        if not order:
            raise ValueError(f"Order with ID {order_id} does not exist")

        if order.fruitType != refund_item:
            raise ValueError(
                f"Refund item mismatch. Ordered item: {order.fruitType}, Refund item: {refund_item}"
            )
        
        if order.buyNumber < refund_quantity:
            raise ValueError("Refund quantity exceeds purchased quantity")

        # Adjust stock
        print(f"Increasing stock for {order.fruitType} by {refund_quantity}")
        self.martRepository.increase_stock(order.fruitType, refund_quantity)

        # Update order
        print(f"Updating order {order_id}: reducing quantity by {refund_quantity}")
        order.buyNumber -= refund_quantity
        order.save()

        return order

