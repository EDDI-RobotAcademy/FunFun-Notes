from librarian.service.librarian_service_impl import LibrarianServiceImpl
from library.service.library_service_impl import LibraryServiceImpl

libraryService = LibraryServiceImpl.getInstance()
librarianService = LibrarianServiceImpl.getInstance()

bookListDisplay = ['Das Kapital', 'The Wealth of Nations',
                    'Guns, Germs, and Steel', 'Sapiens',
                    'Infinity', 'Geometry']
print(bookListDisplay)

# 두명의 사용자가 도서관에서 책을 빌림. 빌린 후 사서에게 보여짐

# 사용자 1
#libraryService.bookChecker()
librarianService.bookShelf()  # 한번 더 입력을 받고, 사서에게 책 이름이 뜸

# 사용자2
#libraryService.bookChecker()
librarianService.bookShelf() # 한번 더 입력을 받고, 사서에게 책 이름이 뜸 







