from abc import ABC, abstractmethod

class LibraryRepository(ABC):

# 도서관에는 어떤 기능이 있나.

    @abstractmethod
    def checkOutBook(self): # 책 대출해주기
        pass
