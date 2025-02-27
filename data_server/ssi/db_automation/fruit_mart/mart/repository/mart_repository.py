from abc import ABC, abstractmethod

class MartRepository(ABC):

    # id로 마트 데이터 조회
    @abstractmethod
    def find_by_fruit_name(self, name):
        pass

    # 모든 마트 데이터 조회
    @abstractmethod
    def find_all(self):
        pass

    # 마트 데이터 생성 및 업데이트
    @abstractmethod
    def save(self, mart):
        pass