class Student:
    def __init__(self, name, id):
        self.name = name # instance variable
        self.id = id # instance variable
    
    # instance method
    def display(self):
        print(f"name: {self.name} and ID: {self.id}")
#==================================
# variable = classname()
student1 = Student("Bob", 11)
student2 = Student("Carol", 22)
print(student1.name, student1.id)
print(student2.name, student2.id)

student1.id = 14
print(student1.name, student1.id)

student1.display()
Student.display(student1)

student2.display()
Student.display(student2)