# Global scope
def calculator(x, y):
    # local scope
    a = 50
    b = 30
    def sum(a, b): 
        res = a + b
        print(res)
    def sub(a, b):
        res = a - b
        print(res)
    sum(a, b)
    sub(b, a)

calculator(10,30)

def age_cal(cur_year, prev_year):
    Age = cur_year - prev_year
    print(Age)

def bmi_cal(hight, weight):
    bmi =  weight / (hight ** 2)
    print(bmi)

def result(age, bmi):
    cur_year = 2025
    prev_year = 2000
    height = 1.7
    weight = 69
    age(cur_year, prev_year)
    bmi(height, weight)

result(age_cal, bmi_cal)



