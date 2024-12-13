from librarian.repository.librarian_repository import LibrarianRepository
from library.service.library_service_impl import LibraryServiceImpl


class LibrarianRepositoryImpl(LibrarianRepository):

    __instance = None

    bookDict = {'Das Kapital': 'Economics', 'The Wealth of Nations': 'Economics',
                'Guns, Germs, and Steel': 'History', 'Sapiens': 'History',
                'Infinity': 'Mathematics', 'Geometry': 'Mathematics'}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def getBookShelf(self, catg1):
        # 단순히 catg를 받아서 bookDict을 검색 후 해당 책의 카테고리를 Dict에 함께 저장
        #database = {}
        #for book in catg1:
        #    if book in self.bookDict.keys():
        #        database.append(book)
        return print(catg1)



        return
