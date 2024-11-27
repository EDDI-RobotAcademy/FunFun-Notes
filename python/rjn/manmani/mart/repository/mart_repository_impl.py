from mart.entity.products import Products
from mart.repository.mart_repository import MartRepository

class MartRepositoryImpl(MartRepository):
    __instance = None

    __products = {}


    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def addProduct(self, name, count):
        if name in self.__products:
            self.__products[name].count += count
        else:
            self.__products[name] = Products(name, count)


    def reduceProduct(self, name: str, count: int):
        if name not in self.__products:
            raise ValueError(f"제품 {name}은 존재하지 않습니다.")
        product = self.__products[name]
        if product.count < count:
            raise ValueError(f"재고가 부족합니다: {name} (요청: {count}, 남은: {product.count})")
        product.count -= count

        if product.count == 0:
            del self.__products[name]

    def getAllProducts(self) :
        productList = []
        for product in self.__products.values():
            productList.append(product)
        return productList
