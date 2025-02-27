from fruit_mart.mart.repository.mart_repository import MartRepository
from fruit_mart.mart.entity.mart import Mart
from fruit_mart.mart.service.mart_service import MartService

class MartServiceImpl(MartService):
    def __init__(self, mart_repository: MartRepository):
        self.mart_repository = mart_repository

    def update_fruit_stock(self, fruit_name, fruit_number):
        mart_list = self.mart_repository.find_all()
        #mart = next((fruit for fruit in mart_list if fruit.fruit_name == fruit_name), None)
        mart = Mart(fruit_name=fruit_name, fruit_number=fruit_number)
        if mart:
            # 기존 과일이 있으면 수량을 더함
            new_fruit_number = mart.fruit_number + fruit_number
            if new_fruit_number < 0:
                raise ValueError("과일 수량이 부족합니다.") #재고 음수 방지
        else:
            # 과일이 없으면 새로운 과일 객체 생성
            mart = Mart(fruit_name=fruit_name, fruit_number=fruit_number)

        # save 메서드 호출 (기존 과일이면 업데이트, 없으면 추가)
        return self.mart_repository.save(mart)

    def get_fruit_by_name(self, fruit_name):
        return self.mart_repository.find_by_fruit_name(fruit_name)

    def get_all_fruits(self):
        return self.mart_repository.find_all()