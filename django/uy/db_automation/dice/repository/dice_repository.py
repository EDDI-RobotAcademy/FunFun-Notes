
from abc import ABC, abstractmethod

class DiceRepository(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def findAll(self):
        pass


    # Repository : 데이터베이스와 상호작용하는 코드 관리
    # 데이터베이스 쿼리를 캡슐화하고, 데이터 저장/ 조회하는 로직을 분리함
    # 주요 기능: 데이터 조회 및 저장, 복잡한 쿼리 로직 분리
    # Django에서는 ORM을 직접 사용하는 경우가 많지만, 복잡한 데이터베이스 작업이 필요할 때 Repository 패턴을 사용하는 경우가 있습니다.