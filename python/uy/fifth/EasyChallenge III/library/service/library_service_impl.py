from library.repository.library_repository_impl import LibraryRepositoryImpl
from library.service.library_service import LibraryService


class LibraryServiceImpl(LibraryService):
    __instance = None
    __borrowedBookList = []

    def __new__(cls):
        if cls.__instance is None:
                cls.__instance = super().__new__(cls)
                cls.__instance.libraryRepository = LibraryRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def bookChecker(self):
        borrowedBook = input("Write the book name you want to check out: ")
        return self.libraryRepository.checkOutBook(borrowedBook)