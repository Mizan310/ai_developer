# list
# list = ['he', 'is', 'a', 'guy']
list = [1, 7, 2, 4, 9, 5]
print(type(list))
list.sort()
print(list)
list1 = sorted(list)
print(list1)
list.append(['a', 'b'])
print(list)
list1.extend([4, 5, 6])
print(list1)

var = list.pop(1)
print(list) # output: [1, 4, 5, 7, 9, 4, 5, 6]
print("Pop value is: ", var) # output: 4

list2 = [1, 7, 2, 4, 9, 5, 7]
list2.remove(2) # Value based
print(list2)
list2.pop(3) # index based
print(list2)

# Count
var = list2.count(7)
print(var)

list3 = [3, "hello", 1]
list4 = list3.copy()
var = list3.pop(1)
print(list3, list4)

list5 = [1, 7, 2, 4, 9, 5, 7]
list5.sort()
print('Sort: ', list5)
list6 = [1, 7, 2, 4, 9, 5, 7]
var = list5.reverse()
print('Reverse',list5)

