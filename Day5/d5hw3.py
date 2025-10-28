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