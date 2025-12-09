from abc import ABC,abstractmethod

class LibraryItem(ABC):
    def __init__(self, isbn):
        self.isbn = isbn
        
    def get_unique_id(self):
         return self.isbn
        
    @abstractmethod
    def check_availability(self):
        pass
    
    
class Book(LibraryItem):
    def __init__(self, title, author, isbn ) -> None:
        self.title = title
        self.author = author
        super().__init__(isbn)
    
    def check_availability(self):
        return True
    
    
class DVD(LibraryItem):
    pass

book = Book("Physics", "masud", 347)

print(book.get_unique_id())
 
dvd = DVD(1234)
