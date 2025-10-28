a = 5
b = 6

def fun1(a, b):
    res = a + b
    return res
def fun2(a, b):
    res2 =  a - b
    return res2
def fun3(a, b):
    res3 = a * b
    return res3
def fun4(a, b):
    res3 = a / b
    return res3

def calculator(a, b):
    var1 = fun1(a, b)
    var2 = fun2(a, b)
    var3 = fun3(a, b)
    var4 = fun4(a, b)
    print(var1, var2, var3, var4)
var =  calculator(a, b)