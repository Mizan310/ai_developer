# non parameterized constructor

class Employee:
    def __init__(self):
        print("Employee object is Created")

emp11 = Employee() # instance 1
emp21 = Employee() # instance 2

# parameterized constructor

class Employee:
    def __init__(self, name):
        self.name = name # instance variable
        print(self.name, "Created")

emp12 = Employee("John") # instance 12
emp22 = Employee("David") # instance 22

class Employee:
    # parameterized constructor
    def __init__(self, name, no):
        self.name = name
        self.no = no
    
    # instance method
    def display(self):
        print(self.name, self.no)

emp13 = Employee("John", 11)
emp23 = Employee("David", 12)
emp13.display()
emp23.display()