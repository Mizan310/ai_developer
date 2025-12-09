# Class is a blueprint for creating instances and unique employee that 
# we create using our employee class will be an instance for that class
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@gmail.com'

    def fullName(self):
        return f'{self.first} {self.last}'

# instance variable

# manually assign 
# emp_1.first = "Mizanur"
# emp_1.last = "Rahman"
# emp_1.email = "MizanurRahman@gmail.com"
# emp_1.pay = 50000

# emp_2.first = "Hasnat"
# emp_2.last = "Hossen"
# emp_2.email = "HasnatHossen@gmail.com"
# emp_2.pay = 50030

emp_1 = Employee("Mizanur", "Rahman", 50000)
emp_2 = Employee("Hasnat", "Hossen", 50030)


# same thing but 
emp_1.fullName() # in there have not declare the argument 
Employee.fullName(emp_1) # but there ahve to declare the argument

print(Employee.fullName(emp_1))

print("###############################")

print(emp_1)
print(emp_2)

print("###############################")

print(f"{emp_1.first} {emp_1.last} has a email no and it is {emp_1.email}")
print(f"{emp_2.first} {emp_2.last} has a email no and it is {emp_2.email}")

print("###############################")

print(emp_1.email)
print(emp_2.email)

print("###############################")

print(emp_1.fullName())
print(emp_2.fullName())

print("###############################")

#same just structural changes are here
print(Employee.fullName(emp_1))
print(Employee.fullName(emp_2))
