#from app.main import bookList
from library.repository.library_repository import LibraryRepository


class LibraryRepositoryImpl(LibraryRepository):

    __instance = None

    __bookList = ['Das Kapital', 'The Wealth of Nations',
                'Guns, Germs, and Steel', 'Sapiens',
                'Infinity', 'Geometry']

    __bookDict = {'Das Kapital': 'Economics', 'The Wealth of Nations': 'Economics',
                  'Guns, Germs, and Steel': 'History', 'Sapiens': 'History',
                  'Infinity': 'Mathematics', 'Geometry': 'Mathematics'}

    __borrowedBook = input("Write the book name you want to check out: ")
    #__bookCategory = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance
        # 싱글톤 패턴


    def checkOutBook(self):  # borrowedBook: 사용자가 원하는 책 이름을 입력해야함
        #borrowedBook = input("Write the book name you want to check out: ")

        if self.__borrowedBook in self.__bookList: #[i]:
            # 사서에게 빌린 책의 이름과, 카테고리 전달 ****
            print("정상적으로 대출 되었습니다.")
            # bookDict에 매칭된 카테고리 불러오기
            if self.__borrowedBook in self.__bookDict:
                categ = self.__bookDict[self.__borrowedBook]
                print(f"대출한 책의 카테고리: {categ}")
        else:
            print("책 이름을 정확하게 입력을 하지 않으면 대출이 불가합니다.")
        return self.__borrowedBook

    # checkOutBook은 빌린 책 이름을 출력


    #def getBorrowedBooK(self):
    #    return self.__borrowedBook