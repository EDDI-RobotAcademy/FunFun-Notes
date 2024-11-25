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

    #두명의 선수 이름 받기
    def Sign(self):
        a=int(input("몇명이세요: "))
        #입력받은 만큼 선수인원 생성


        #인원만큼 for돌리기
        for i in range(a):
            self.name=input("Insert your name:")
            #선수이름 받기
            player=self.name
            #player에 선수이름 넣기
            people=Player(player)
            #people에 Player클래스에 player값 넣은 결과 넣기
            self.__team.append(people)
            #team리스트에 결과 넣기

    #리스트값 출력
    def acquireTeam(self):
        return self.__team

