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

    # 현재 Aggregate Root 형태로 Entity가 구성된 경우
    # OuterRef, Subquery, Coalesce 사용이 필요합니다.
    # OuterRef의 경우 서브쿼리에서 외부 쿼리의 필드를 참조할 수 있도록 만듬
    # 즉 현재 엔티티 외의 엔티티 값을 필터링하고자 하는 경우 사용함
    # Subquery의 경우엔 특정 조건에 맞는 데이터를 외부 엔티티와 결합할 때 사용
    # Coalesce의 경우엔 NULL인 경우 대체값을 반환하도록 구성하는 목적으로 사용
    def list(self, page=1, perPage=12):
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
