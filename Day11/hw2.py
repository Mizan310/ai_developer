class Library:
    def __init__(self):
        self._catalog = []
        
    
    def add_book(self, book):
        self._catalog.append(book)
    def get_total_books(self):
        for i in self._catalog:
            print(i)
        

library1 = Library()
library1.add_book("Physics")
library1.add_book("Math")
library1.add_book("Bangla")

library1.get_total_books() 