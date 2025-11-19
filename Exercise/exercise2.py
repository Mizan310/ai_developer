# You are given a 2D list. Make a Python function that will return a 1D list preserving the elements’ position.
# Child lists should have the same length; if not, raise a proper error.

numbers = [[1,2,3,4], [3,4,5,6], [5,6,7,8]]

flattened = []

for item in numbers:
    if type(item) == list:
        for i in item: # iterating through each element of child list
            if type(i) == list:
                for j in i: # iterating through each element of sub-child list
                    flattened.append(j) # appending each element to flattened list
            else:
                flattened.append(i) # appending each element to flattened list
    else:
        flattened.append(item) # appending each element to flattened list

print("Flattened list: ", flattened)

# By calling recursive function
def flatten_list(nested_list):
    flat = []
    for item in nested_list:
        if type(item) == list:
            flat.extend(flatten_list(item)) # recursively calling the function for sub-lists
        else:
            flat.append(item)
    return flat
numbersss = [[1,[2,3],[4,6]], [3,4,5,6], [5,6,7,8]]
result = flatten_list(numbersss)
print("Flattened list: ", result)

# python compiler
list_2d = [[1,2,3],
           [4,5,6],
           [7,8,9]]
list_1d = []

for i in range(len(list_2d)): # iterating through rows
    for j in range(len(list_2d[0])): # iterating through columns
        list_1d.append(list_2d[i][j]) # appending each element to 1D list

print(list_1d)




