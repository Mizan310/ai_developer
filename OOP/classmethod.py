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

    @classmethod #decorator
    def set_raise_amnt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    
emp_1 = Employee("Mizanur", "Rahman", 50000)
emp_2 = Employee("Hasnat", "Hossen", 50030)

# for set_raise_amnt method:

# Employee.raise_amount = 1.05

Employee.set_raise_amnt(1.05)
# emp_1.set_raise_amnt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# first, last, pay = emp_str_1.split("-")
# new_emp_1 = Employee(first, last, pay)

print("Number of Employees", Employee.num_of_emps)

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.first, new_emp_1.last, new_emp_1.pay)
