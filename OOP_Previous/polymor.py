# Polymorphism - 
# Same method name, in different class, act as a different way..
#   
class Student:
    def __init__(self, name, grade, percentage): # This is fun/method
        self.name = name # attribute, self.name = property(name)
        self.grade = grade # attribute, self.name = property(grade)
        self.percentage = percentage # attribute, self.name = property(grade)

    def student_details(self): # method
        print(f"{self.name} is in class {self.grade} and the percentage is {self.percentage}")

# object - instances of class
student1 = Student("Madhav", 11, 89)
student2 = Student("Rahman", 12, 98)

# child Class
class GraduateStudent(Student): 
    def __init__(self, name, grade, percentage, stream): 
        super().__init__(name, grade, percentage) 
        self.stream = stream 

    def student_details(self): # method - polymorphism (Same *method name* as before)
        # Without super method
        print(f'{self.name} is in {self.grade} class and got avg {self.percentage} and from stream is {self.stream}')

    def student_details(self): # method - inheritance
        super().student_details()
        print(f'Stream is {self.stream}')

# object - from Student class
student1 = Student("Madhav", 11, 89)

# object - from GraduateStudent class
Grad_stu1 = GraduateStudent('Adnan', 12, 96, 'PCM')
# print(Grad_student1.stream)

student1.student_details() # it calling parent method
Grad_stu1.student_details() # by calling polymorphism function also inheritance function(because it is enabled)