## **Problem-6**
# Write a program that iterates through the numbers from a given list. Print "even" for even numbers and "odd" for odd numbers.

# **Example:**
# Input: [4, 2, 7, 8, 1]
# Output:
# 4: even
# 2: even
# 7: odd
# 8: even
# 1: odd

numbers = [4, 2, 7, 8, 1]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

        