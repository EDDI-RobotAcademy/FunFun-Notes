from inventory.repository.inventory_repository_impl import InventoryRepositoryImpl

inventoryRepository = InventoryRepositoryImpl.getInstance()

inventoryRepository.addProduct("오렌지", 5)
inventoryRepository.addProduct("사과", 3)


print("현재 재고 상태:")
for product in inventoryRepository.getAllProducts():
    print(product)


print("\n사과 3개 구매")
inventoryRepository.reduceProduct("사과", 2)

for product in inventoryRepository.getAllProducts():
    print(product)
