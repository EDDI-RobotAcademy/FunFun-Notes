from mart.repository.mart_repository_impl import MartRepositoryImpl

martRepository = MartRepositoryImpl.getInstance()
martRepository.addFruit('Apple',5)
martRepository.printCurrentStatus()



