""""
Task 1: The Basic Book
Create a class named Book.
Define the constructor (__init__) to accept title, author, and isbn (International Standard Book Number).
Set title and author as public attributes (self.title).
Set the isbn as a private attribute (self.__isbn).
Add a public method called get_isbn that safely returns the private __isbn attribute.
Test: Create a Book object and try to access its title and its isbn (show why direct access to __isbn fails).
"""

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn

    def get_isbn(self):
        return self.__isbn
    
    def __repr__(self):
        return f"{self.title} by {self.author} ans ISBN is {self.__isbn}"
 
'''
Task 2: The Library Catalog
Create a class named Library.
Define the constructor (__init__) that initializes a protected attribute called self._catalog to an empty list (this list will store Book objects).
Add a method add_book(book) that takes a Book object and appends it to the self._catalog list.
Add a method get_total_books that returns the length of the self._catalog list.
Test: Create 3 Book objects, create a Library object, add the books to the library, and print the total count.
'''
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

'''
Task 3: Specialized Book Types
Create a class named Magazine that inherits from Book.
Define the Magazine constructor to accept title, author, isbn, and a new, unique attribute called issue_number.
Inside Magazine.__init__:
Use super().__init__(...) to pass the title, author, and isbn up to the Book parent class.
Initialize the unique issue_number attribute.
Add a method get_type to Magazine that returns the string "Magazine"Test: Create one Book and one Magazine. Show that the Magazine object can still call the inherited get_isbn method.
'''
class Magazine(Book):
    def __init__(self, title, author, isbn, issue_number):
        super().__init__(title, author, isbn)
        self.issue_number = issue_number

    def get_type(self):
        return "Magazine: "

'''
Task 4: The Patron (User)
Create a class named Person.
Define the constructor to accept and set name and member_id.
Create a class named Librarian that inherits from Person.
The Librarian constructor should:Use super() to handle name and member_id.
Add a unique attribute called hire_date.
Test: Create a Librarian object and confirm it correctly initializes both the inherited member_id and the unique hire_date.
'''
class Person:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

class Librarian(Person):
    def __init__(self, name, member_id, hire_date):
        super().__init__(name, member_id)
        self.hire_date = hire_date


'''
Task 5: The Checkout Protocol (Overriding)
In the original Book class (the parent), add a public method called display_info(). This method should print: "Title: {title} by {author}".
In the inherited Magazine class (the child), override the display_info() method.
The overridden method should:Call the parent's display_info() method using super().display_info() to print the title and author.
Then, print the unique attribute: "Issue Number: {issue_number}".
Test: Create a Book object and a Magazine object, and call display_info() on both to show the different outputs from the same method name.
'''
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn

    def get_isbn(self):
        return self.__isbn
    
    def __repr__(self):
        return f"{self.title} by {self.author} ans ISBN is {self.__isbn}"

    # task - 5
    def display_info(self):
        print(f"{self.title} by {self.author}") 

class Magazine(Book):
    def __init__(self, title, author, isbn, issue_number):
        super().__init__(title, author, isbn)
        self.issue_number = issue_number

    def get_type(self):
        return "Magazine: "
    
    # task - 5
    def display_info(self):
        super().display_info()
        print("Issue Number: ", self.issue_number)

'''
Task 6: The Abstract Loan Processor
In the Library class, add a method called loan_item(item) that takes either a Book or a Magazine object.
This method should polymorphically call the object's display_info() method.
Use a list called inventory = [book_instance, magazine_instance].
Use a for loop to iterate over the inventory list and call loan_item(item) for each one.
Goal: This loop should seamlessly call the correct, customized display_info() for each type of item, demonstrating that the code works generally (polymorphically).
'''
class Library:
    def __init__(self):
        self._catalog = []
    
    def add_book(self, book):
        self._catalog.append(book)
    
    def get_total_books(self):
        return len(self._catalog)
    
    def loan_item(self, item):
        print("Loned item info: ")
        item.display_info()

'''
Task 7: The Abstract Library Item

Goal: Create an abstract blueprint that forces all inventory items to have a unique ID and a method for checking availability.
Import ABC and abstractmethod from the abc module.
Define an Abstract Base Class (ABC) called LibraryItem that inherits from ABC.
Define a regular method in LibraryItem called get_unique_id(self) that simply returns the item's ID (e.g., self.isbn or some other internal ID).
Define an abstract method using the @abstractmethod decorator called check_availability(self). This method should contain only pass (as it has no implementation here).
Test: Try to create an object directly from LibraryItem (e.g., item = LibraryItem()). The student should observe that this correctly raises a TypeError.
'''
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def get_unique_id(self):
        return self.isbn

    @abstractmethod
    def check_availability(self):
        pass

'''
Task 8: Implementing the Abstract Protocol

Goal: Modify the existing Book class to adhere to the abstract contract and demonstrate that the system now enforces it.
Modify the Book class from Task 1 so that it inherits from LibraryItem (e.g., class Book(LibraryItem):).
Implement the abstract method check_availability(self) inside the Book class. This method should return a simple boolean value, like True for available.
Test 1 (Success): Create a Book object and call the inherited non-abstract method get_unique_id() and the implemented abstract method check_availability().
Test 2 (Failure): Create a new class, DVD, that inherits from LibraryItem but fails to implement check_availability(). Attempt to instantiate a DVD object and observe that it correctly raises a TypeError, proving the abstract contract is enforced.
'''

from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, isbn):
        self.__isbn = isbn

    def get_unique_id(self):
        return self.__isbn

    @abstractmethod
    def check_availability(self):
        pass

class Book(LibraryItem):
    def __init__(self, title, author, isbn):
        super().__init__(isbn)
        self.title = title
        self.author = author
        # self.__isbn = isbn

    def get_isbn(self):
        return self.__isbn
    
    def __repr__(self):
        return f"{self.title} by {self.author} ans ISBN is {self.__isbn}"

    # task - 5
    def display_info(self):
        print(f"{self.title} by {self.author}")

    def check_availability(self):
        return "True"


# task - 1
book = Book("Learn Python", "Tamim", 1206)
# print("Title: ", book.title)
# print("Author: ", book.author)
# print("ISBN: ", book.get_isbn())
# print("ISBN: ", book.__isbn)
# print(book)

# Task-2
library = Library()
    
book1 = Book("Learn Python", "Tamim", 1206)
book2 = Book("Learn C program", "Tamim", 1205)
book3 = Book("Learn C++ program", "Tamim", 1207)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
# print("Total Books", library.get_total_books())

book4 = Book("Learn C#", "Tamim", 1205)
book5 = Book("Learn Java", "Tamim", 1207)
library.add_book(book4)
library.add_book(book5)
# print("Total Books", library.get_total_books())

# library.show_all_books()

# task 3
test_book = Book("Python Basics", "John Doe", 5001)
# print(test_book)

test_magazine = Magazine("Tech Monthly", "Jane Smith", 6001, 42)
# print(f"{test_magazine.get_type()}{test_magazine} and its issue number is: {test_magazine.issue_number}")
# print(test_magazine.get_isbn())
# print(test_magazine.get_type())
# print("Issue Number is: ", test_magazine.issue_number)

# task - 4
librarian1 = Librarian("Brian", 101, "01/01/2025")
# print(librarian1.member_id)
# print(librarian1.hire_date)

# task - 5

book6 = Book("The Secret", "Ron D. Byron", 11045)
magaz = Magazine("Kishor Alo", "Prothom Alo", 111, 34)

# book6.display_info()
# magaz.display_info()

# task - 6
inventory = [book4, magaz]
# library = Library()
for item in inventory:
    library.loan_item(item)

# task - 7
# item = LibraryItem()

# task - 8

book7 =  Book("Iranishi", "Anisul", 12334)
print(book7.get_unique_id())
print(book7.check_availability())

