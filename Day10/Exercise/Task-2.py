class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn

    def get_isbn(self):
        return self.__isbn
    
    def __repr__(self):
        return f"{self.title} by {self.author} ans ISBN is {self.__isbn}"

class Library:
    def __init__(self):
        self._catalog = []
    
    def add_book(self, book):
        self._catalog.append(book)
    
    def get_total_books(self):
        return len(self._catalog)
    
    def show_all_books(self):
        for book in self._catalog:
            print(book)

class Magazine(Book):
    def __init__(self, title, author, isbn, issue_number):
        super().__init__(title, author, isbn)
        self.issue_number = issue_number

    def get_type(self):
        return "Magazine: "
    
book = Book("Learn Python", "Tamim", 1206)
# print("Title: ", book.title)
# print("Author: ", book.author)
# print("ISBN: ", book.get_isbn())
# print(book.__isbn)
print(book)

library = Library()
    
book1 = Book("Learn Python", "Tamim", 1206)
book2 = Book("Learn C program", "Tamim", 1205)
book3 = Book("Learn C++ program", "Tamim", 1207)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
print("Total Books", library.get_total_books())

book4 = Book("Learn C#", "Tamim", 1205)
book5 = Book("Learn Java", "Tamim", 1207)
library.add_book(book4)
library.add_book(book5)
print("Total Books", library.get_total_books())

library.show_all_books()
