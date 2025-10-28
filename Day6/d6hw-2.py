# hw-2
# you are given a list of numbers
# your output will be a list containing the indices of the odd numbers

lst = [10, 21, 4, 45, 66, 93, 11]
for index in range(len(lst)):
    if lst[index] % 2 == 0:
        continue
    else:
        print(f"Index of odd number {lst[index]} is {index}")