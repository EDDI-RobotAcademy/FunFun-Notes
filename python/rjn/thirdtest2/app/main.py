from player.repository.player_repository_impi import PlayerRepositoryImpl

playerRepository = PlayerRepositoryImpl.getInstance()


player1 = playerRepository.pickName()
player2 = playerRepository.pickName()


print(player1,player2)