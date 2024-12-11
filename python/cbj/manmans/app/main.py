from buyer.service.buyer_service_impl import BuyerServiceImpl
from fruit.repository.fruit_repository_impl import FruitRepositoryImpl

buyer_service = BuyerServiceImpl.getInstance()


fruit_repo = FruitRepositoryImpl.getInstance()
fruit_repo.create("apple", 20)
fruit_repo.create("orange", 15)


buyer_service.buyFruit("apple", 5)
buyer_service.buyFruit("orange", 20)
buyer_service.buyFruit("pear", 3)