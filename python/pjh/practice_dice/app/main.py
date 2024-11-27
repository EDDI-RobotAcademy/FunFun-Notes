# 과일 싱글톤 생성 : 과일 이름 input, 과일 개수 input
# 구매자 생성 : 구매자 이름 input, 구매할 과일 이름 Input, 구매할 과일 개수 input
# 구매자가 과일 구매 : 과일 개수 - 구매한 과일 개수
# 최종 남은 과일 재고 리스트 추출

item = ItemRepositoryImpl.getInstance()
item.createItem()
item.createItem()
print(ItemRepository.itemlist())