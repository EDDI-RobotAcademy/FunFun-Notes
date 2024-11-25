from player.repository.player_repository_impl import player_RepositoryImpl

# player1 = Player('Kim')  # Kim
# player2 = Player('Lee')  # Lee

playerRepository = player_RepositoryImpl.getInstance()
# getInstance()로 player_RepositoryImpl를 가져와야 함.
playerRepository.createName('Kim')  # 매개변수가 name 한개 뿐, 그리고. createName 자체가 객체를 생성함.
playerRepository.createName('Lee')

playerList = playerRepository.getUserList()

for player in playerList:
    print(player)




