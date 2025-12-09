class Person:
    def __init__(self, name, member_id) -> None:
        self.name = name
        self.member_id = member_id
        

class Librarian(Person):
    def __init__(self, name, member_id, hire_date) -> None:
        super().__init__(name, member_id)
        self.hire_date = hire_date


librarian = Librarian("Masud", 62, 122989823)


print(librarian.name) 
print(librarian.member_id)    
   