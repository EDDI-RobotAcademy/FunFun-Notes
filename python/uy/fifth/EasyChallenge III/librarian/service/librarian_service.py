from abc import ABC, abstractmethod

class LibrarianService(ABC):

    @abstractmethod
    def bookShelf(self):
        pass
