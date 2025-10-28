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