from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from game_software.entity.game_software import GameSoftware
from game_software.repository.game_software_repository import GameSoftwareRepository


class GameSoftwareRepositoryImpl(GameSoftwareRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self, page=1, perPage=12):
        everyList = self.findAll()
        paginator = Paginator(everyList, perPage)

        try:
            paginatedData = paginator.page(page)
        except PageNotAnInteger:
            paginatedData = paginator(1)
        except EmptyPage:
            paginatedData = []

        return paginatedData, paginator.num_pages

    def findAll(self):
        return GameSoftware.objects.all()
    