class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn

    def get_isbn(self):
        return self.__isbn
    
book = Book("Learn Python", "Tamim", 1206)

print(book.get_isbn())
print(book.__isbn) # Because it is private
