from abc import ABC,abstractmethod

class LibraryItem(ABC):
    def __init__(self, isbn):
        self.isbn = isbn
    def get_unique_id(self):
         return self.isbn
        
    @abstractmethod
    def check_availability(self):
        pass
    

libraryItem = LibraryItem()
    
    
    