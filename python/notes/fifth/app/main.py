import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

print("PYTHONPATH:", sys.path)

from customer.service.customer_service_impl import CustomerServiceImpl
from mart.entity.fruit import Fruit
from mart.service.mart_service_impl import MartServiceImpl
from order.service.order_service_impl import OrderServiceImpl

martService = MartServiceImpl.getInstance()
martService.loadFruit(Fruit.APPLE, 3)
martService.loadFruit(Fruit.ORANGE, 5)
fruitList = martService.fruitMapList()
print(f"현재 저희 매장에 남은 과일은: {fruitList}")

customerService = CustomerServiceImpl.getInstance()
geniusPYDId = customerService.createCustomer('딩코재천박예닮')

orderService = OrderServiceImpl.getInstance()
orderService.buyFruit(Fruit.APPLE, 2, geniusPYDId)

fruitList = martService.fruitMapList()
print(f"주문 이후 매장에 남은 과일은: {fruitList}")

orderService.orderList(geniusPYDId)
