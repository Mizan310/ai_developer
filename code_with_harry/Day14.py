a = int(input("Enter age: "))
print("Age is: ", a)

if(a>18):
    print("You can drive")
    print("Yes")
else:
    print("You cannot drive.")
    print("No")

appple_price = 210
budget = 200
if(appple_price<=budget):
    print("Buy it")
else:
    print("do nit add this in the chart")

# Nested elif:
num = 13
if(num<0):
    print("Number is Negative")
elif(num>0):
    if(num<=10):
        print("NUmber is between 1-10")
    elif(num>10 and num<=20):
        print("NUmber is between 11-20")
    else:
        print("Number is grater than 20")
else:
    print("Number is Zero")