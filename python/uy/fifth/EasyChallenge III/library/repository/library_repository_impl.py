from library.repository.library_repository import LibraryRepository


class LibraryRepositoryImpl(LibraryRepository):

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
        # 싱글톤 패턴


    def checkOutBook(self, borrowedBook):  # borrowedBook: 사용자가 원하는 책 이름을 입력해야함
        catg = []  # 사서에게 전달할 대출된 책의 카테고리 리스트

        if borrowedBook in self.bookDict.keys():
            # 사서에게 빌린 책의 이름과, 카테고리 전달 ****
            print(f"{borrowedBook}이 정상적으로 대출 되었습니다.")
            catg.append(borrowedBook)
        else:
            print("책 이름을 정확하게 입력을 하지 않으면 대출이 불가합니다.")

        return catg
