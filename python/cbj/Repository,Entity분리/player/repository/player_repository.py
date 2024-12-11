from abc import ABC, abstractmethod


class PlayerRepository(ABC):

    @abstractmethod
    def rollPlayerNicknameList(self):
        pass
