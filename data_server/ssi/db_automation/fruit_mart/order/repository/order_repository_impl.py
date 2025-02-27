from fruit_mart.order.entity.order import Order

class OrderRepositoryImpl:
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

    def create(self, customer, fruit, number):
        order = Order(
            customerNickName=customer, 
            fruitType=fruit, 
            buyNumber=number
        )
        order.save()
        return order

    def findAll(self):
        return Order.objects.all()

    def findById(self, id):
        return Order.objects.get(id=id)

    def findByFruit(self, fruit):
        return Order.objects.filter(fruitType=fruit).first()

    def findByNumber(self, number):
        return Order.objects.filter(buyNumber=number).first()

    def findByCustomer(self, customer):
        return Order.objects.filter(customerNickName=customer)
