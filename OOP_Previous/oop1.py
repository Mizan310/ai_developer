# student details
# student_1 = ['Madhav', 10] # Name:, Grade: (list)
# student_2 = ['Karim', 12]
# student_3 = ['Rahim', 11]
# student_4 = ['Vshakha', 12]

# print(student_1)
# print(student_1[0])
# print(f"{student_1[0]} is in class {student_1[1]}")
# print(f"{student_2[0]} is in class {student_2[1]}")

# using oops- creating student records


# class - blueprint -- or template
# __init__ --> object er value initialize e help korbe
# self er kaj --> class er sathe object er connection build kore
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
# print(student1.name, student1.grade)


student2 = Student("Rahman", 12, 98)
# print(student2.name, student2.grade)

# print(student1.percentage) # we can print like that way
student1.student_details() # object.method - it call the method my passing class parameters abd print the method
student2.student_details()

# or if we want to print as a dictionary then --->
# print(student1.__dict__)

# modify object property/attribute
print(student1.percentage)
student1.percentage = 98 # modify
print(student1.percentage)

# delete object property
print(student1.__dict__)
del student1.percentage
print(student1.__dict__)

# delete object
# del student1
# print(f"{student1} is deleted")



