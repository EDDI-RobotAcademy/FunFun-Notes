from abc import ABC, abstractmethod

class PlayerRepository(ABC):
    @abstractmethod
    def pickYourRandomNickname(self):
        pass
