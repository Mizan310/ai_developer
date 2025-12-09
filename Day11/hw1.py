class Book:
    def __init__(self, title, author, isbn ) -> None:
        self.title = title
        self.author = author
        self.__isbn = isbn
        
    def get_isbn(self):
        return self.__isbn
    
books = Book("Physics", "masud", 23)
print(books.get_isbn())

#Return Error 
print(books.__isbn)