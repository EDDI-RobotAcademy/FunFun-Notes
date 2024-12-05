

class Library:

    # 1. 도서관에 있는 책 목록
    __bookDict = {'Das Kapital':'Economics','The Wealth of Nations':'Economics',
                  'Guns, Germs, and Steel':'History', 'Sapiens': 'History',
                  'Infinity':'Mathematics', 'Geometry' :'Mathematics'}

    def __init__(self): # 외부에서 받을 게 있나? - 일단 다 적고 나중에 수정
        # 필요없는것 같기도....
        self.__categoryEconomics = self.__bookDict[0][1] #'Economics'
        self.__categoryHistory = self.__bookDict[1][1]   # 'History'
        self.__categoryMathematics = self.__bookDict[2][1]  # 'Mathematics'
        self.__book1 = self.__bookDict[0][0] #'Das Kapital'
        self.__book2 = self.__bookDict[1][0] # 'The Wealth of Nations'
        self.__book3 = self.__bookDict[2][0] # 'Guns, Germs, and Steel'
        self.__book4 = self.__bookDict[3][0] # 'Sapiens'
        self.__book5 = self.__bookDict[4][0] # 'Infinity'
        self.__book6 = self.__bookDict[5][0] # 'Geometry'


        # 책 목록을 먼저 프린트하고, 도서관 이용자는 책 목록에서 책을 input으로 넣음
        # 대출 되었습니다. 문구와 책 카테고리를 함께 반환한다.


