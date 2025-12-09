# ============================================
# TASK 1: THE BASIC BOOK CLASS
# ============================================

class Book:
    """Book class with public and private attributes"""
    
    def __init__(self, title, author, isbn):
        """
        Initialize a Book object
        
        Args:
            title: Book title (public attribute)
            author: Book author (public attribute)
            isbn: ISBN number (private attribute)
        """
        self.title = title      # Public attribute
        self.author = author    # Public attribute
        self.__isbn = isbn      # Private attribute (name mangling with __)
    
    def get_isbn(self):
        """Public method to safely access the private ISBN"""
        return self.__isbn
    
    def __str__(self):
        """String representation of the book"""
        return f"'{self.title}' by {self.author} (ISBN: {self.__isbn})"


# ============================================
# TASK 2: THE LIBRARY CATALOG CLASS
# ============================================

class Library:
    """Library class to manage a catalog of books"""
    
    def __init__(self):
        """Initialize the library with an empty catalog (protected attribute)"""
        self._catalog = []  # Protected attribute (single underscore)
    
    def add_book(self, book):
        """Add a Book object to the catalog"""
        self._catalog.append(book)
        print(f"✓ Added to library: {book}")
    
    def get_total_books(self):
        """Return the total number of books in the catalog"""
        return len(self._catalog)
    
    def display_catalog(self):
        """Display all books in the catalog"""
        if not self._catalog:
            print("The library catalog is empty.")
        else:
            print("\n" + "="*60)
            print("LIBRARY CATALOG")
            print("="*60)
            for i, book in enumerate(self._catalog, 1):
                print(f"{i}. {book}")
            print("="*60)


# ============================================
# TESTING THE CLASSES
# ============================================

if __name__ == "__main__":
    print("="*60)
    print("TASK 1: TESTING THE BOOK CLASS")
    print("="*60)
    
    # Create a Book object
    book = Book("Learn Python", "Tamim Shahriar", 1206)
    
    # Access public attributes (this works!)
    print(f"\nAccessing public attributes:")
    print(f"  Title: {book.title}")
    print(f"  Author: {book.author}")
    
    # Access ISBN through the public method (correct way)
    print(f"\nAccessing ISBN through get_isbn() method:")
    print(f"  ISBN: {book.get_isbn()}")
    
    # Try to access private __isbn directly (this will fail!)
    print(f"\nTrying to access private __isbn directly:")
    try:
        print(f"  book.__isbn = {book.__isbn}")
    except AttributeError as e:
        print(f"  ❌ ERROR: {e}")
        print(f"  → Direct access to private attribute __isbn fails!")
    
    # Explain name mangling
    print(f"\nExplanation:")
    print(f"  The private attribute __isbn is name-mangled to _Book__isbn")
    print(f"  This prevents accidental access from outside the class.")
    print(f"  Actual mangled name: {book._Book__isbn} (not recommended to use!)")
    
    
    print("\n" + "="*60)
    print("TASK 2: TESTING THE LIBRARY CLASS")
    print("="*60)
    
    # Create 3 Book objects
    print("\nCreating 3 books...")
    book1 = Book("Learn Python", "Tamim", 1206)
    book2 = Book("Learn C program", "Tamim", 1205)
    book3 = Book("Learn C++ program", "Tamim", 1207)
    
    # Create a Library object
    print("\nCreating a library...")
    library = Library()
    
    # Add books to the library
    print("\nAdding books to the library:")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    # Print the total count
    print(f"\n{'='*60}")
    print(f"TOTAL BOOKS IN LIBRARY: {library.get_total_books()}")
    print(f"{'='*60}")
    
    # Display the complete catalog
    library.display_catalog()
    
    
    print("\n" + "="*60)
    print("ADDITIONAL DEMONSTRATIONS")
    print("="*60)
    
    # Add more books
    print("\nAdding 2 more books...")
    book4 = Book("Data Structures and Algorithms", "Robert Sedgewick", 1208)
    book5 = Book("Introduction to Algorithms", "CLRS", 1209)
    library.add_book(book4)
    library.add_book(book5)
    
    print(f"\nTotal books now: {library.get_total_books()}")
    
    # Display updated catalog
    library.display_catalog()
    
    # Demonstrate accessing protected attribute (not recommended but possible)
    print("\n" + "="*60)
    print("ACCESSING PROTECTED ATTRIBUTE _catalog")
    print("="*60)
    print("Protected attributes (single underscore) can be accessed but shouldn't be:")
    print(f"Number of books via _catalog: {len(library._catalog)}")
    print("Note: This is discouraged! Use get_total_books() method instead.")
    
    
    print("\n" + "="*60)
    print("SUMMARY OF ACCESS MODIFIERS")
    print("="*60)
    print("1. Public (no underscore): self.title")
    print("   → Accessible from anywhere")
    print("\n2. Protected (single underscore): self._catalog")
    print("   → Convention: for internal use, but still accessible")
    print("\n3. Private (double underscore): self.__isbn")
    print("   → Name mangling applied, not directly accessible")
    print("="*60)