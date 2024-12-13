from librarian.repository.librarian_repository_impl import LibrarianRepositoryImpl
from librarian.service.librarian_service import LibrarianService
from library.service.library_service_impl import LibraryServiceImpl


class LibrarianServiceImpl(LibrarianService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
                cls.__instance = super().__new__(cls)
                cls.__instance.libraryService = LibraryServiceImpl.getInstance()
                cls.__instance.librarianRepository = LibrarianRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def bookShelf(self):
        catg1 = self.libraryService.bookChecker() # 여기서 catg가 옴
        return self.librarianRepository.getBookShelf(catg1)

