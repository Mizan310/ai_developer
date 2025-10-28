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