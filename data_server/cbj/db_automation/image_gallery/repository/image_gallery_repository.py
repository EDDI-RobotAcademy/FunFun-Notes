from abc import ABC, abstractmethod


class ImageGalleryRepository(ABC):

    @abstractmethod
    def list(self, page, perPage):
        pass
