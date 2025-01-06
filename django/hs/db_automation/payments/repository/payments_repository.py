from abc import ABC, abstractmethod


class PaymentsRepository(ABC):

    @abstractmethod
    def request(self, paymentRequestData):
        pass
