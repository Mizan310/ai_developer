class Book:
    def __init__(self, title, author, isbn ) -> None:
        self.title = title
        self.author = author
        self.__isbn = isbn
        
    def get_isbn(self):
        return self.__isbn


class Magazine(Book):
    def __init__(self, title, author, isbn, issue_number) -> None:
        super().__init__(title, author, isbn)
        self.issue_number = issue_number
        
    def get_type(self):
        return "Magazine"
    
mgazine = Magazine("Physics", "masud", 23, 78)
print(mgazine.get_isbn())
    