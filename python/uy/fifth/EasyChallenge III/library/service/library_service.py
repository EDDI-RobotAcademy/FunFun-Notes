from abc import ABC, abstractmethod


# 책 빌려주기
class LibraryService(ABC):

    @abstractmethod
    def bookChecker(self):  # LibrarianRepositoryImpl에서 가져옴. 빌린 책을 사서가 볼수 있다.
        pass
