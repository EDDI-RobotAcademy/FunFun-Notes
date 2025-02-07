from customer.repository.customer_repository_impl import CustomerRepositoryImpl
from customer.service.customer_service import CustomerService


class CustomerServiceImpl(CustomerService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__customerRepository = CustomerRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createCustomer(self, name):
        return self.__customerRepository.create(name)
    