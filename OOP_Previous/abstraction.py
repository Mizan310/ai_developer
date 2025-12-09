# Abstraction --> this method hiding unnecessary details from users through classes, methods


class Student:
    def __init__(self, name, grade, percentage): # This is fun/method
        self.name = name # attribute, self.name = property(name)
        self.grade = grade # attribute, self.name = property(grade)
        self.percentage = percentage # attribute, self.name = property(grade)

    # Abstraction method hiding unnecessary details from users through classes, methods
    def student_details(self): # method - abstraction
        print(f"{self.name} is in class {self.grade} and the percentage is {self.percentage+2}%") # Hidden from users


# object - instances of class
student1 = Student("Mizanur", 11, 89)
# print(student1.name, student1.grade)

student2 = Student("Rahman", 12, 96)
# print(student2.name, student2.grade)

# print(student1.percentage) # we can print like that way

# print(student1.team)
student1.student_details() # object.method - it call the method my passing class parameters abd print the method
student2.student_details()