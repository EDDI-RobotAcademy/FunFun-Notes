from customer.entity.customer import Customer
from customer.repository.customer_repository import CustomerRepository


class CustomerRepositoryImpl(CustomerRepository):
    __instance = None

    __customerList = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, name):
        customer = Customer(name)
        self.__customerList.append(customer)

        return customer.getId()

    def findById(self, id):
        for customer in self.__customerList:
            if customer.getId() == id:
                return customer

        return None
