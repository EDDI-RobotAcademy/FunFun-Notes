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
        # 아무런 옵션이 없으면 1페이지, 12개씩 보여주기
        # GameSoftware의 Price(가격) 정보를 획득하기 위해 구성하였음
        # 실제 GameSoftwarePrice에 gameSoftare에 해당하는 pk 값 중 price 값과 일치되는 것을 뽑아옴
        # 결론적으로 GameSoftware의 pk(고유값인 id)를 참조하여 일치하는 정보의 price를 획득함
        # filter가 걸려 있으므로 모든 정보(Entity 개수만큼)에 대해 위의 작업이 진행됨
        priceSubQuery = GameSoftwarePrice.objects.filter(gameSoftware=OuterRef('pk')).values('price')[:1]
        # 여기도 동일하게 GameSoftwareImage에 GameSoftware에 해당하는 pk값을 찾고
        # 여기서 image에 해당하는 정보(values('image')[:1]) 1개를 획득함
        # 마찬가지로 filter 이므로 모든 Entity에 대해 적용됨
        imageSubQuery = GameSoftwareImage.objects.filter(gameSoftware=OuterRef('pk')).values('image')[:1]

        # GameSoftware Entity에 추가적인 항목을 추가하는 작업으로 annotate가 붙음
        # 앞서 구성한 priceQuery를 통해 가격 정보를 획득
        # Coalesce를 통해 정보가 없는 경우 0으로 대체
        # image에 대해서도 동일하게 처리
        # 다만 정보가 없는 경우 빈 공백으로 처리함
        gameSoftwareList = GameSoftware.objects.annotate(
            price=Coalesce(Subquery(priceSubQuery), Value(0)),
            image=Coalesce(Subquery(imageSubQuery), Value('')),
        )

        paginator = Paginator(gameSoftwareList, perPage)

        try:
            paiginatedGameDataList = paginator.page(page)
        except PageNotAnInteger:
            paiginatedGameDataList = paginator.page(1)
        except EmptyPage:
            paiginatedGameDataList = []

        paginatedGameSoftwareList = [
            {
                'id': game.id,
                'title': game.title,
                'price': game.price,
                'image': game.image,
            }
            for game in paiginatedGameDataList
        ]

        return paginatedGameSoftwareList, paginator.num_pages

    def findAll(self):
        return GameSoftware.objects.all()

    def create(self, title):
        return GameSoftware.objects.create(title=title)
