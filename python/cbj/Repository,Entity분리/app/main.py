from player.repository.player_repository_impl import (PlayerRepositoryImpl)

playerRepository = PlayerRepositoryImpl.getInstance()
# 주사위를 2개 굴리기
playerRepository.rollPlayerNicknameList()
playerRepository.rollPlayerNicknameList()
# 굴린 주사위 리스트 획득
playerNicknameList = playerRepository.acquirePlayerNicknameList()
print("here")

# 주사위 리스트를 순회하며 출력
# for *추출정보 in 리스트' <- 이러한 형태로 사용할 수 있습니다.
for player in playerNicknameList:
    print(player)