from mart.mart_repository.mart_repository_impl import MartRepositoryImpl

martRepository = MartRepositoryImpl.getInstance()
martRepository.addFruit('Apple', 3)
martRepository.printCurrentStatus()



# xxxDomainRepository = XxxDomainRepositoryImpl.getInstance()
# xxxDomainRepository.뭐하고싶어1(필요하면_배치하거나_전달할_요소들_없어도됨)
# xxxDomainRepository.뭐하고싶어2()
