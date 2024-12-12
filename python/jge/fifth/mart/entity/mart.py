#재고 자체를 관리
class Stock:
    def __init__(self, name: str, stock: int):
        self.name = name
        self.stock = stock
    #재고 추가
    def add_stock(self, quantity: int):
        self.stock += quantity
    #재고 제거? 감소
    def reduce_stock(self, quantity: int):
        if self.stock < quantity:
            raise ValueError(f"재고가 부족합니다. 현재 남은 갯수: {self.stock}")
        self.stock -= quantity

class Mart:
    # 재고 이름이랑 갯수 딕셔너리로 묶을거
    def __init__(self):
        self.items = {}
    #마트에 아이템 새 재고를 추가
    def add_item(self, item: Stock):
        self.items[item.name] = item
    # 재고 조회
    def get_item(self, name: str):
        #if 부분 현재 재고종류는 서비스에서 구현?
        if name not in self.items:
            raise ValueError(f"해당 상품이 없습니다. 현재 재고 종류:{', '.join(self.items.keys())}")
        return self.items[name]
    def purchase_item(self, name: str, quantity: int):
        if name not in self.items:
            raise ValueError(f"{name}은 마트에 없습니다. 현재 재고 종류: {', '.join(self.items.keys())}")

        item = self.items[name]  # 재고 찾기
        item.reduce_stock(quantity)  #마트 재고 감소
        return f"{name} {quantity}개 구매하셨습니다. 현재 남은 갯수: {item.stock}개"


'''
mart = Mart()

apple = Item("사과",10)
orange = Item("오렌지",6)

mart.add_item(apple)
mart.add_item(orange)

apple_item = mart.get_item("사과")  # 사과 조회
apple_item.reduce_stock(3)  # 3개 구매
print(f"사과 3개 구매 후 남은 재고: {apple_item.stock}개")
'''




