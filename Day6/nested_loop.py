ls1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in ls1:
    print(i[1]) # it print the middle element of the each sublist
    for j in i:
        print(j, end=' ')
    print()
