from abc import ABC, abstractmethod

class LibrarianRepository(ABC):

    @abstractmethod
    def bookChecker(self):  # 빌린 책을 사서가 볼수 있다.
        pass

    @abstractmethod
    def getBorrowedBookList(self):
        pass