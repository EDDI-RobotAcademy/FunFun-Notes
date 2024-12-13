from mart.repository.mart_repository import MartRepository
from mart.entity.mart import Stock

#여기서 초기 재고데이터 관리
class MartRepositoryImpl(MartRepository):
    def __init__(self):
        self.items = {} #아무것도 없는 상태 미리 사과,오렌지 추가해도되긴함.

    def add_item(self, item: Stock):
        self.items[item.name] = item

    def get_item(self, name: str):
        return self.items[name]