from abc import ABC, abstractmethod

class LibrarianRepository(ABC):

    @abstractmethod
    def getBookShelf(self):
        pass