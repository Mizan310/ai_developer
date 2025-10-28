# Assignment operator
# +, -, *, /, %
# //, **

# num1 = 30.98
# num2= 2
# result = num1 / num2
# print(result)
# print(x - y)

# main_price = 10000
# percent_discount = 10

# percentage_amount_discount = main_price*percent_discount/100

# print("Main price is: ", + main_price - percentage_amount_discount)


user1_amount = float(input("Enter the amount of the user: "))
discount_percentage = float(input("Enter the discount in percentage: "))

percentage_discount = user1_amount*(discount_percentage/100)

total_result = user1_amount - percentage_discount
print(f"You got {discount_percentage} and you have to pay {total_result}")