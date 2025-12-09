class Book:
    def __init__(self, title, author, isbn ) -> None:
        self.title = title
        self.author = author
        self.__isbn = isbn
        
    def get_isbn(self):
        return self.__isbn
    
    def  display_info(self):
        print(f"{self.title} : {self.author}")


class Magazine(Book):
    def __init__(self, title, author, isbn, issue_number) -> None:
        super().__init__(title, author, isbn)
        self.issue_number = issue_number
        
    def get_type(self):
        return "Magazine"

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")


class Library:
    def __init__(self) -> None:
        self._catalog = []
        
    
    def add_book(self, book):
        self._catalog.append(book)
    def get_total_books(self):
        for i in self._catalog:
            print(i)
    def loan_item(self, item):
        item.display_info()
        
        
book_instance = Book("Physics", "masud", 23)
book_instance = Magazine("Physics", "masud", 23, 78)

library = Library()

inventory  = [book_instance, book_instance]

for i in inventory:
    library.loan_item(i)