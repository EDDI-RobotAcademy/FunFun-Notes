from player.repository.player_repository_impl import player_RepositoryImpl

# player1 = Player('Kim')  # Kim
# player2 = Player('Lee')  # Lee

playerRepository = player_RepositoryImpl.getInstance()
playerRepository.createName('Kim')
playerRepository.createName('Lee')

playerList = playerRepository.getUserList()

for player in playerList:
    print(player)




