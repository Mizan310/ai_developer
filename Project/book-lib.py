class Book:
    def __init__(self, title, author, isbn, password):
        self.title = title
        self.author = author
        self.__isbn = None # initially empty
        self.set_isbn(isbn)
        self.__password = password

    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, value):
        if len(str(value)) == 4:
            self.__isbn = value
        else:
            print("Invalid ISBN")

    def update_isbn_secure(self, new_value, password_input):
        if password_input == self.__password:
            self.set_isbn(new_value)
            print("ISBN updated successfully")
        else:
            print("Incorrect password! ISBN update failed.")

title = input("Enter the book name: ")
author = input("Enter the author name: ")
isbn = int(input("Enter 4-digit ISBN: "))
password = input("Set a password for the security: ")

book = Book(title, author, isbn, password)

print("\n--- Book Information ---")
print("Title: ", book.title)
print("Author: ", book.author)
print("ISBN: ", book.get_isbn())

# print(book.get_isbn())
# print(book.__isbn) # Because it is private
# print(book.__dict__)

print("\n--- Update ISBN (Secure) ---")
given_pass = input("Enter password to update ISBN: ")

new_isbn = input("\nEnter new ISBN to update: ")

book.update_isbn_secure(new_isbn, given_pass)

print("Title: ", book.title)
print("Author: ", book.author)
print("ISBN: ", book.get_isbn())