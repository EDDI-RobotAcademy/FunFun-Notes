from fruit_mart.repository.fruit_mart_repository_impl import FruitMartRepositoryImpl
from order.service.order_service_impl import OrderServiceImpl

orderService = OrderServiceImpl.getInstance()
orderService.createOrder()

fruitMartRepository = FruitMartRepositoryImpl.getInstance()
fruitMartRepository.fruit_stock()