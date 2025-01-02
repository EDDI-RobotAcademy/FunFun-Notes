from abc import ABC, abstractmethod


class PaymentsService(ABC):

    @abstractmethod
    def process(self):
        pass
