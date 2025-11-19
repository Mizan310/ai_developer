items = [[1,2,3], 
         [3,2,1], 
         [2,2,2],
         [1,2,3]]

row_avg = []
count = 0
for row in items:
    total = 0
    count = 0
    for num in row:
        total += num
        count += 1
    avg = total / count
    row_avg.append(avg)
print("Average of row: ", row_avg)

col_avg = []
num_rows = len(items) 
# counts how many lists (rows) are inside the outer list.
# (because there are 3 inner lists — each one is a row)
# That’s why we don’t use an index — we want the count of all rows directly.
num_cols = len(items[0])
# Each inner list (items[0], items[1], etc.) represents a row.
# We assume each row has the same number of columns, so we can just take the first one (items[0]) to check how many columns there are.
# (because [10, 20, 30] has 3 elements — 3 columns)
# That’s why here we need [0] — we have to go inside one of the rows to see how many columns it has.
for c in range(num_cols):
    total = 0
    count = 0
    for r in range(num_rows):
        total += items[r][c]
        count += 1
    avg = total/count
    col_avg.append(avg)
print("Average of column: ", col_avg)

# python compiler
list = [[1,2,3],
        [3,2,1],
        [2,2,2],
        [1,2,3]]
row_avg = []
for i in list:
    row_avg.append(sum(i)/len(i))
    

col_avg = []
sum = 0

for i in range(0,len(list[0])):
    for j in range(0,len(list)):
       sum+=list[j][i]
    col_avg.append(sum/len(list))
    sum = 0

final = []

final.append(row_avg)
final.append(col_avg)

print(final)

