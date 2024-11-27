from player.repository.player_repository import PlayerRepository
from player.entity.player import Player

class PlayerRepositoryImpl(PlayerRepository):
    __instance = None
    __team=[]
    #team리스트 생성

    def __new__(cls):
        #진짜 생성자 생성
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance
    #싱글톤 생성

    #선수 이름 받기
    def __Sign(self):
        userName=input("INSERT YOUR NAME:")
        return userName

    def createName(self):
        user=self.__Sign()
        player=Player(user)
        self.__team.append(player)

    #리스트값 출력
    def acquireTeam(self):
        return self.__team

    #플레이어 Id찾기
    def findId(self,id):
        for player in self.__team:
            if player.getId()==id:
                return player
        return None