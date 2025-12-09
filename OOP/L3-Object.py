class Student:
    def __init__(self, name, id):
        self.name = name # instance variable
        self.id = id # instance variable
        # print("A student is working")
#==================================
# variable = classname()
student1 = Student("Bob", 11)
student2 = Student("Carol", 22)
print(student1.name, student1.id)
print(student2.name, student2.id)

student1.id = 14
print(student1.name, student1.id)
