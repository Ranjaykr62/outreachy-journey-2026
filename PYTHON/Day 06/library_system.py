# challenge_library.py
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"{self.title} by {self.author} - {status}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in library")
            return
        for b in self.books:
            b.display()

    def search(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                return b
        return None

    def borrow(self, title):
        book = self.search(title)
        if book and book.available:
            book.available = False
            print(f"You borrowed: {book.title}")
        else:
            print("Book not available")

    def return_book(self, title):
        book = self.search(title)
        if book and not book.available:
            book.available = True
            print(f"You returned: {book.title}")
        else:
            print("Return failed or book not found")

# example
lib = Library()
b1 = Book("Python 101", "Author A")
b2 = Book("Data Science", "Author B")
lib.add_book(b1)
lib.add_book(b2)
lib.display_books()
lib.borrow("Python 101")
lib.display_books()
lib.return_book("Python 101")
lib.display_books()
