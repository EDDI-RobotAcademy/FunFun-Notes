from google.protobuf.service import Service
from librarian.repository.librarian_repository_impl import LibrarianRepositoryImpl
from librarian.BookSaveService.BookSaveService_repository import BookSaveServiceRepository
from library.repository.library_repository_impl import LibraryRepositoryImpl


class BookSaveServiceRepositoryImpl(BookSaveServiceRepository):
    __instance = None
    __borrowedBookList = []

    def __new__(cls):
        if cls.__instance is None:
                cls.__instance = super().__new__(cls)
                cls.__instance.__LibraryRepository = LibraryRepositoryImpl.getInstance()
                cls.__instance.__LibrarianRepository = LibrarianRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def bookSaveService(self):
        #createdDrink = self.__drinkRepository.create()
        book= self.__LibraryRepository.checkOutBook()
                            # return: 사용자가 빌린 책 이름을 출력
        self.__borrowedBookList.append(book)
        # 사용자가 책을 빌림 :borrowedBook 이걸 borrowedBookList에 저장해서 목록을 관리함
        # 생성된 음료 서빙 요청
		#self.__serveRepository.serveDrink(createdDrink)
        #borrowedBookList.bookChecker()
        #borrowedBookList.getBorrowedBookList()
        print(self.__borrowedBookList)
        #return borrowedBookList


    def bookChecker(self):
        pass

    def checkOutBook(self):
        pass

    def getBorrowedBookList(self):
        pass


