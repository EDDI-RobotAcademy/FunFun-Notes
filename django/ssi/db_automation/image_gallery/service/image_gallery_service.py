from abc import ABC, abstractmethod


class ImageGalleryService(ABC):

    @abstractmethod
    def requestList(self, page, perPage):
        pass