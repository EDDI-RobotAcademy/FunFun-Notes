#오늘 몇개의 과일이 들어왔나
#그 과일들이 몇개 들어왔나

from fruit.entity.fruit import Fruit
from fruit.repository.fruit_repository import FruitRepository
from fruit.repository.fruit_repository_impl import FruitRepositoryImpl

martOpen=FruitRepositoryImpl.getInstance()
martOpen.createFruit()
martOpen.AllList()
