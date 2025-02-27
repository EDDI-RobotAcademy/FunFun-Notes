from abc import ABC, abstractmethod

class MartService(ABC):
    # 과일 재고 업데이트
    @abstractmethod
    def update_fruit_stock(self, fruit_name, fruit_number):
        pass

    @abstractmethod
    def get_fruit_by_name(self, fruit_name):
        pass

    @abstractmethod
    def get_all_fruits(self):
        pass