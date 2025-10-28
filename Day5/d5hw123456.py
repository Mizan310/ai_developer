## **Problem-1**
# Write a program that takes a list of integers and finds all the numbers that appear more than once. Print the repeated numbers and their frequencies.

# Example:
# Input: [1, 2, 3, 2, 4, 5, 6, 5, 5, 7, 8]

# Output:
# Repeated numbers and their counts:
# 2: 2
# 5: 3
nums = eval(input("Enter the list of a number: "))
counts = {}
for n in nums:
    counts[n] = counts.get(n, 0) + 1
print("repeated num and their counts: ")
for key, value in counts.items():
    if value > 1:
        print(f"{key}: {value}")

## **Problem-2**

# Write a program that takes two lists of integers. Then, find and print:

# 1. The elements common to both.
# 2. The elements that are unique to each.

# **Example:**
# Input: list1 = [1, 2, 3, 4], list2 = [3, 4, 5, 6]
# Output:
# Common elements: {3, 4}
# Unique to list1: {1, 2}
# Unique to list2: {5, 6}

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

set1 = set(list1)
set2 = set(list2)

common = set1 & set2
unique = set1 ^ set2

print(common)
print(unique)

## **Problem-3**
# Write a function that accepts a string and 
# counts the number of vowels 
# (a, e, i, o, u, case-insensitive).

# **Example:**
# Input: "Hello World from Python"
# Output:
# Number of vowels: 5

text = input()
vowles = "aeiouAEIOU"

count = 0
for ch in text:
    if ch in vowles:
        count = count + 1

print("Number of Vowels: ", count)

## **Problem-4**
# You are given a list of tuples, where each tuple contains two items: a name (string) and a score (integer).
# Write a program that sorts the list of tuples based on the score in increasing order.

# **Example:**
# Input: [('John', 85), ('Jane', 92), ('David', 78), ('Emily', 92)]

# Output: [('David', 78), ('John', 85), ('Jane', 92), ('Emily', 92)]

students = [('John', 85), ('Jane', 92), ('David', 78), ('Emily', 92)]

for i in range(len(students)):
    for j in range(i + 1, len(students)):
        if students[i][1] > students[j][1]:
            temp = students[i]
            students[i] = students[j]
            students[j] = temp

print(students)

## **Problem-5**

# Write a function that merges two dictionaries. Keys can be different. If a key exists in both dictionaries, sum their values.

# **Example:**
# Input: d1 = {'a': 100, 'b': 200, 'c': 300}, d2 = {'a': 300, 'b': 200, 'd': 400}
# Output: {'a': 400, 'b': 400, 'c': 300, 'd': 400}

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

marged = d1.copy()

for key, value in d2.items():
    if key in marged:
        marged[key] += value
    else:
        marged[key] = value

print(marged)

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

        