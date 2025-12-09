# Encapsulation --> Restrict access to certain attributes or methods to predict data and enforce controlled access

class Student:
    def __init__(self, name, grade, percentage): # This is fun/method
        self.name = name # attribute, self.name = property(name)
        self.grade = grade # attribute, self.name = property(grade)
        self.__percentage = percentage # attribute, self.name = property(grade) # double underscore, limits access (private kore rakha)
    
    # Restrict access to certain attributes or methods to predict data and enforce controlled access
    def get_percentage(self): # method - encapsulation
        return self.__percentage

    def student_details(self): 
        # if self.__percentage >= 70:
        #     print(f"{self.name} is in class {self.grade} and the percentage is {self.__percentage}%.")
        # else:
        #     # If the percentage is less than 70, don't print it
        #     print(f"{self.name} is in class {self.grade}.")

        print(f"{self.name} is in class {self.grade} and the percentage is {self.__percentage}%") 


# object - instances of class
student1 = Student("Mizanur", 11, 89)
# print(student1.name, student1.grade)

student2 = Student("Rahman", 12, 67)
# print(student2.name, student2.grade)

# print(student1.__percentage) # we can print like that way

# print(student1.team)
student1.student_details() # object.method - it call the method my passing class parameters abd print the method
student2.student_details()

print("Only percentage 1 ",student1.get_percentage())
print("Only percentage 2 ",student2.get_percentage())