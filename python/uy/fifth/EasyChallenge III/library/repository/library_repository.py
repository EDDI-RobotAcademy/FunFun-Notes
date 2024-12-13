from abc import ABC, abstractmethod

class LibraryRepository(ABC):


    @abstractmethod
    def checkOutBook(self): # 책 대출해주기
        pass
