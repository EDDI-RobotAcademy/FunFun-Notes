from abc import ABC, abstractmethod

class BookSaveServiceRepository(ABC):

    @abstractmethod
    def bookChecker(self):  # LibrarianRepositoryImpl에서 가져옴. 빌린 책을 사서가 볼수 있다.
        pass

    @abstractmethod
    def checkOutBook(self):  # LibraryRepositoryImpl에서 가져옴. 책 대출해주기
        pass

    @abstractmethod
    def getBorrowedBookList(self):
        pass
