from librarian.BookSaveService.BookSaveService_repository_impl import BookSaveServiceRepositoryImpl
from library.repository.library_repository_impl import LibraryRepositoryImpl
from librarian.repository.librarian_repository_impl import LibrarianRepositoryImpl

libraryRepository = LibraryRepositoryImpl.getInstance()
librarianRepository = LibrarianRepositoryImpl.getInstance()
bookSaveServiceRepository = BookSaveServiceRepositoryImpl.getInstance()

# Agenda 설계

# 사용자를 위해서 book list 제시
bookListDisplay = ['Das Kapital', 'The Wealth of Nations',
                    'Guns, Germs, and Steel', 'Sapiens',
                    'Infinity', 'Geometry']
print(bookListDisplay)

# 1. 도서관에서 책을 2권 빌림, 카테고리도 함께 출력
#libraryRepository.checkOutBook()
#libraryRepository.checkOutBook()

# 3. **빌린 책은 사서가 볼 수 있습니다.  -> DB에 정보를 넣는 개념(?)
#librarianRepository.bookChecker()
bookSaveServiceRepository.bookSaveService()
#bookSaveServiceRepository.getBorrowedBookList()
bookSaveServiceRepository.bookSaveService()
#bookSaveServiceRepository.getBorrowedBookList()





