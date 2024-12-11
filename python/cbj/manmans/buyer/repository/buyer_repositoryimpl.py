from buyer.entity.buyer import Buyer
from buyer.repository.buyer_repository import BuyerRepository

class BuyerRepositoryImpl(BuyerRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__buyer = Buyer("부대찌개")

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, name):
        pass

buyer = Buyer("부대찌개")