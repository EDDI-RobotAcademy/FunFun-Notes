from librarian.repository.librarian_repository import LibrarianRepository


class LibrarianRepositoryImpl(LibrarianRepository):

    __instance = None

    __borrowedBookList = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    # 관리자 페이지에 책 내용 전달
    # 사용자가 도서를 입력하면 자동으로 borrowedBook에 저장되고, 사서에게 보여짐.
    def bookChecker(self, borrowedBook):
        self.__borrowedBookList.append(borrowedBook)


    # __borrowedBookList 리턴이 필요함
    def getBorrowedBookList(self):
        return self.__borrowedBookList