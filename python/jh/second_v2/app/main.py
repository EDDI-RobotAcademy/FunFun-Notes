from player.repository.player_repository_impl import (PlayerRepositoryImpl)

# 주사위 도메인 없이 플레이어 하나가 주사위 굴리기

playerRepository = PlayerRepositoryImpl.getInstance()

for i in range(10):
    playerRepository.rollPlayerDiceList()

# 굴린 주사위 리스트 획득
playerDiceList = playerRepository.acquirePlayerDiceList()
print("here\n")
print(*playerDiceList)

# 주사위 리스트를 순회하며 출력
# for *추출정보 in 리스트' <- 이러한 형태로 사용할 수 있습니다.
for diceNum in playerDiceList:
    print(diceNum)