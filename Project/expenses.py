# 𝗣𝗲𝗿𝘀𝗼𝗻𝗮𝗹 𝗘𝘅𝗽𝗲𝗻𝘀𝗲 𝗧𝗿𝗮𝗰𝗸𝗲𝗿 - Simple Decision Making → income এর সাথে খরচ compare
# 𝐃𝐚𝐭𝐚 𝐒𝐭𝐨𝐫𝐞 করতে হবে (𝐋𝐢𝐬𝐭 + 𝐃𝐢𝐜𝐭𝐢𝐨𝐧𝐚𝐫𝐲)

# expenses = [
#     {'category': 'Food', 'amount': 25000},
#     {'category': 'transport', 'amount': 1200},
#     {'category': 'Shopping', 'amount': 5000},
#     {'category': 'Food', 'amount': 15000},
#     {'category': 'Rent', 'amount': 20000},
#     {'category': 'Rent', 'amount': 23000},
#     {'category': 'Tuition fees', 'amount': 15000}
# ]

expenses = []
n = int(input("How many expenses in this month: "))
for i in range(n):
    print(f"\nExpense {i+1}")
    category = input("Category: ")
    amount = float(input("Amount: "))
    expenses.append({'category': category, 'amount': amount})
print(expenses)
totalExpenses = 0
for item in expenses:
    totalExpenses += item['amount']

print(f"\nTotal expense is: {totalExpenses}")


category_wise = {} # একটি খালি dictionary বানানো হলো। এখানে আমরা category অনুযায়ী খরচ জমাবো।
for item in expenses: #list এর প্রতিটি dictionary এক এক করে নেবে।
    category = item['category'] # dictionary থেকে category বের করা হলো।
    amount = item['amount'] # dictionary থেকে amount বের করা হলো।
    if category in category_wise: # check করে দেখা হচ্ছে যে category আগে থেকেই dictionary তে আছে কি না।
        category_wise[category] = category_wise.get(category, 0) + amount
        # category_wise[category] += amount # যদি category থাকে → আগের value এর সাথে নতুন amount যোগ করবে।
    else: # যদি category না থাকে → নতুন category add করবে।
        category_wise[category] = amount # নতুন category তৈরি হলো এবং amount বসানো হলো।
print("Category wise cost: ", category_wise, "\n")
#########################################
print("\n")

for category in category_wise:
    amount = category_wise[category]
    print("Category wise Cost of", category, amount)
print("\n")

# for item in category_wise.items():
#     category = item[0]
#     amount = item[1]
#     print("Print - 2", category, amount)
# print("\n")

# for category in category_wise.keys():
#     amount = category_wise[category]
#     print("Print - 3", category, amount)
# print("\n")

# for amount in category_wise.values():
#     print("Print - 4", amount)
# print("\n")

#########################################

# income = 100000
income = int(input("Enter the monthly income: "))
savings = income - totalExpenses
if savings > 0:
    print(f"Yeah I have some money after cost of everything {savings}") 
elif savings == 0:
    print(f"I can't save but it is okay")
else:
    print(f"I have to need more money, it is about {abs(savings)}")

highest_category = None
highest_amount = 0
for category, amount in category_wise.items():
    if amount > highest_amount:
        highest_amount = amount
        highest_category = category
print(f"Most expenses category is {highest_category} and cost is {highest_amount} of money")