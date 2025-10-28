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