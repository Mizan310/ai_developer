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
 
 
        
books = Book("Physics", "masud", 23)
books.display_info()

magazine = Magazine("Physics1", "masud1", 23, 78)
magazine.display_info()