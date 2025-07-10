class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.available=True
    def borrow(self):
        #Check if the book is there to borrow
        if self.available:
            self.available=False
            print("Book borrowed")
        else:
            print("Book not available")
    def return_book(self):
        if not self.available:
            self.available=True
            print("Book returned")
    def display(self):
        if self.available:
            print(f"Name: {self.title}"
                  f"Author: {self.author}")
class Library:
    def __init__(self):
        self.all_books=[]
    def add_book(self,book):
        self.all_books.append(book)
    def display(self):
        for book in self.all_books:
            book.display()
    def borrows(self,title):
        for boo in self.all_books:
            if boo.title == title:
                boo.borrow()
                return
    def return_books(self,title):
        for book in self.all_books:
            if book.title == title:
                book.return_book()

book1=Book("B1","Author")
lib=Library()
lib.add_book(book1)
book2=Book("B2","Author")
lib.add_book(book2)
lib.borrows("B1")
lib.return_books("B1")
lib.display()


