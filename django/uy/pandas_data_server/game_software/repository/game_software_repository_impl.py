from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import OuterRef, Subquery, Value
from django.db.models.functions import Coalesce

from game_software.entity.game_software import GameSoftware
from game_software.entity.game_software_image import GameSoftwareImage
from game_software.entity.game_software_price import GameSoftwarePrice
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
        # 아무런 옵션이 없으면 1페이지 12개씩 보여주기
        # GameSoftware의 Price 정보를 획득하기 위해 구성한 것임
        # 실제 GameSoftwarePrice의 gameSoftware에 해당하는 pk값 중 price 값과 일치되는 것을 뽑아옴
        priceSubQuery = GameSoftwarePrice.objects.filter(gameSoftware=OuterRef('pk')).values('price')[:1]
        imageSubQuery = GameSoftwareImage.objects.filter(gameSoftware=OuterRef('pk')).values('image')[:1]

        gameSoftwareList = GameSoftware.objects.annotate(
            price=Coalesce(Subquery(priceSubQuery), Value(0)),
            image=Coalesce(Subquery(imageSubQuery), Value('')),
        )

        paginator = Paginator(gameSoftwareList, perPage)

        try:
            paiginatedGameDataList = paginator.page(page)
        except PageNotAnInteger:
            paiginatedGameDataList = paginator(1)
        except EmptyPage:
            paiginatedGameDataList = []

        paginatedGameSoftwareList = [
            {
                'id': game.getId(),
                'title': game.getTitle(),
                'price': game.getPrice(),
                'image': game.getImage(),
            }
            for game in paiginatedGameDataList
        ]

        return paginatedGameSoftwareList, paginator.num_pages

    def findAll(self):
        return GameSoftware.objects.all()
