from mart.repository.mart_repository_impl import MartRepositoryImpl

martRepository = MartRepositoryImpl.getInstance()

martRepository.addProduct("오렌지", 5)
martRepository.addProduct("사과", 3)


print("현재 재고 상태:")
for product in martRepository.getAllProducts():
    print(product)

print("\n")
print("사과 3개 구매")
martRepository.reduceProduct("사과", 2)

for product in martRepository.getAllProducts():
    print(product)
