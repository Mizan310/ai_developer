class Employee:
    num_of_emps = 0 # class variables
    raise_amount = 1.04 # class variables
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

        Employee.num_of_emps += 1

    def full_name(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 
    
emp_1 = Employee("Mizanur", "Rahman", 50000)
emp_2 = Employee("Hasnat", "Hossen", 50030)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# emp_1.raise_amount = 1.05 # instance variable
# Employee.raise_amount = 1.05 # instance variable
# print(emp_1.__dict__)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

print("Number of Employees", Employee.num_of_emps) # 2