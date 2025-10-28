# for loop
# Iterable 
# len function 

items = ['i1', 'i2', 'i3', 'i4']
for i in items:
    print(i)

# Sequence tyep data - list, string, tuple, we can use them for the for loop

list1 = [4, 3, 1, 5]

for i in list1:
    print(i)

for i in range(len(list1)): # range is used to generate sequence of numbers
    print(list1[i], i)

for i in 'hello':
    print(i)

# nirdhisto program ke nirdisto number er jonno call 
for i in range(5): # 5 means 0 to 4
    print(i, "Hello world")

for i in range(1, 6): # 6 means 1 to 5
    print(i, "- Hello world")

# step argument
for i in range(1, 8, 2): # 2 means step of 2
    print(i, "- Hello") 

print(list(range(1,8)))
print(list(range(1,8,2)))

# reverse order
for i in range(10, 0, -1):
    print(i)

for i in range(5):
    print("Outer loop", i)
    for j in range(3):
        print("   Inner loop", j)

# pyramid pattern

n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()
# end="" parameter is userd to avoid new line after each print
# n = int(input("Enter number of rows: "))
for i in range(n-1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
m = int(input("Enter number: "))
for i in range(1, m+1):
    print('*' * i, end='\n')
for i in range(m-1, 0, -1):
    print('*' * i, end='\n')


n = int(input("Enter a number: "))
print(list(range(0, n+1, 1)))
print(list(range(n, -1, -1)))
print(list(range(1, n+1, 1)))
print(list(range(n, 0, -1)))

for i in range(1, n+1):
    print(i, end=' ') # output: 1 2 3 4 5
print()

# hw-1
n = int(input("Enter number of rows: "))
for i in range(1, n):
    for j in range(n-i):
        print(" ", end='')
    for k in range(i):
        print("* ", end='')
    print()

for i in range(1, n):
    for j in range(i):
        print(" ", end='')
    for k in range(n - i):
        print("*", end=' ')
    print()

#     * 
#    * *
#   * * *
#  * * * *
#  * * * *
#   * * *
#    * *
#     *

# hw-2
# you are given a list of numbers
# your output will be a list containing the indices of the odd numbers

# lst = [10, 21, 4, 45, 66, 93, 11]
# odd_indices = []
# for index in range(len(lst)):
#     if lst[index] % 2 == 0:
#         continue
#     odd_indices.append(index)
#     print(f"Index of odd number {lst[index]} is {index}")
#     print(odd_indices)

lst = [10, 21, 4, 45, 66, 93, 11]
for index in range(len(lst)):
    if lst[index] % 2 == 0:
        continue
    else:
        print(f"Index of odd number {lst[index]} is {index}")





