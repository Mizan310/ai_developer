# init is used to construct or create a new object 
# class React:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# React(2, 3)

# add dunder method

str1 = "Hello"
str2 = "World"
# new_str = str1 + str2
new_str = str1.__add__(" " + str2)
print(new_str)

new_str2 = new_str.__len__()
print(new_str2)

