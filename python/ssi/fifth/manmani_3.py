class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.author}'이(가) {self.tile} 적음 ({self.category})"

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self,book):
        if not book.is_borrowed:
            self.borrowed_books.append(book)
            book.is_borrowed = True
            print(f"{self.name}이(가) {book.title}을 빌렸습니다.")
        else:
            print(f"누군가가 이미 {book.title}을(를) 빌림")

    def return_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
            print(f"{self.name}이(가) {book.title}을(를) 반납함")
        else:
            print(f"{self.name}이(가) {book.title}을 가지고 있지 않음")

    def __str__(self):
        return f"사용자: {self.name}, 빌린 책: {[book.title for book in self.borowed_books]}"

class Librarian:
    def __init__(self):
        self.borrowed_books = {}  #uwer
        self.returned_books = []  #반납된 책 목록

    def manage_borrow(self, user, book):
        if user not in self.borrowed_books:
            self.borrowed_books[user] = []
        self.borrowed_books[user].append(book)

    def manage_return(self, user, book):
        if user in self.borrowed_books and book in self.borrowed_books[user]:
            self.borrowed_books[user].remove(book)
            self.borrowed_books.append(book)

    def view_borrowed_books(self):
        print("빌려준 책들: ")
        for user, books in self.borrowed_books.items():
            print(f"{user.name}이(가) {[book.title for book in books]}을(를) 빌려감")

    def view_returned_books(self):
        print("반납된 책들 :")
        for user, books in self.borrowed_books.items():
            print(f"{user.name}이(가) {[book.title for book in books]}을 반납함")

class Library:
    def __init__(self):
        self.books = []
        self.users = {}
        self.librarian = Librarian()

    def add_book(self, book):
        self.books.append(book)
        print(f"책 '{book.title}'이(가) 추가됨")

    def removw_book(self, book_title):
        for book in self.books:
            if book.title == book_title and not book._is_borrowed:
                self.books.remove(book)
                print(f"책 '{book.title}'을(를) 버림")
                return
        print(f"책 '{book_title}'은 버릴 수 없음.(누군가가 빌리고 있는 책이거나 존재하지 않는 책임)")

    def list_books(self):
        print("현재 있는 책들: ")
        for book in self.books:
            if not book.is_borrowed:
                print(book)

    def borrow_book(self, user_name, book_title):
        if user_name not in self.users:
            print(f"사용자 '{user_name}'이(가) 존재하지 않음")
            return
        user = self.users[user_name]
        for book in self.books:
            if book.title == book_title and not book.is_borrowed:
                user.borrow_book(book)
                self.librarian.manage_borrow(user, book)
                return
        print(f"책 '{book_title}'은(는) 빌릴수 없습니다")

    def return_book(self, user_name, book_title):
        if user_name not in self.users:
            print(f"사용자 '{user_name}'이(가) 존재하지 않음")
            return
        user = self.users[user_name]
        for book in user.borrowed_books:
            if book.title == book_title:
                user.return_book(book)
                self.librarian.manage_return(user, book)
                return
        print(f"{user_name}은(는) 책 '{book_title}'을 가지고 있지 않습니다")

    def add_user(self, name):
        if name in self.users:
            print(f"사용자 '(name)'이 이미 존재합니다")
        else:
            self.users[name] = User(name)
            print(f"사용자 '{name}'이(가) 추가됨")

    def remove_user(self, name):
        if name in self.users:
            if self.users[name].borrowed_books:
                print(f"사용자 '{name}'이(가) 현재 빌리고 있는 책이 있음. 사용자 삭제 불가")
            else:
                del self.users[name]
                print(f"사용자 '{name}'의 정보를 삭제함")

    def list_users(self):
        print("사용자 목록: ")
        for name, user in self.users.items():
            print(user)

def main():
    library = Library()

    # 초기 책 데이터 추가
    library.add_book(Book("The Wealth of Nations", "Adam Smith", "Economy"))
    library.add_book(Book("Sapiens", "Yuval Noah Harari", "History"))
    library.add_book(Book("1984", "George Orwell", "Fiction"))

    while True:
        print("\n--- Library Menu ---")
        print("1. 사용자 추가")
        print("2. 사용자 정보 삭제")
        print("3. 사용자 목록")
        print("4. 책 목록")
        print("5. 책 빌리기")
        print("6. 책 반납")
        print("7. 책 추가")
        print("8. 책 버리기")
        print("9. 빌린 책 목록")
        print("10. 반납 책 목록")
        print("11. 종료")
        choice = input("하고자 하는 행동: ")

        if choice == "1":
            name = input("추가할 사용자 이름: ")
            library.add_user(name)
        elif choice == "2":
            name = input("삭제할 사용자 이름: ")
            library.remove_user(name)
        elif choice == "3":
            library.list_users()
        elif choice == "4":
            library.list_books()
        elif choice == "5":
            user_name = input("당신의 이름을 입력하시오: ")
            book_title = input("빌리고자 하는 책의 제목을 입력하시오: ")
            library.borrow_book(user_name, book_title)
        elif choice == "6":
            user_name = input("당신의 이름을 입력하시오: ")
            book_title = input("반납하고자 하는 책 제목을 입력하시오: ")
            library.return_book(user_name, book_title)
        elif choice == "7":
            title = input("추가하고자 하는 책 제목을 입력하시오: ")
            author = input("책 저자의 이름을 입력하시오: ")
            category = input("책의 분야를 입력하시오: ")
            library.add_book(Book(title, author, category))
        elif choice == "8":
            book_title = input("버릴 책 이름을 입력하시오: ")
            library.remove_book(book_title)
        elif choice == "9":
            library.librarian.view_borrowed_books()
        elif choice == "10":
            library.librarian.view_returned_books()
        elif choice == "11":
            print("도서관 관리 시스템 종료!")
            break
        else:
            print("지원하지 않는 기능입니다. 다시 시도해 주세요")

if __name__ == "__main__":
    main()