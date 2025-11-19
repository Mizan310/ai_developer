# Core concept

# Real world scenarios are objectified in the programming language
# object: existance
# Shither pitha: receipe/blueprint--> no existance --> class
# Chitoi pitha: existance --> object, class er instance
# 4 piller 
# Inheritance
# Encapsulation
# Polymorphism
# Abstraction

# init works as a constructor

# class Pitha:
#     def __init__(self, name, taste):
#         print(name, taste)
#     pass

# chitoi = Pitha("Chitoi pitha", "Multi-test")
# print(chitoi)

# vapa = Pitha("vaba", "Sweet")
# print(vapa)

class Pitha:
    def __init__(self, name, taste):
        # print(name, taste)
        self.name = name
        self.taste = taste
    # Method
    def taste_is(self):
        x = self.taste
        print(f"{self.name} pitha has {x}")
    pass

# Object/instance: chitoi
chitoi = Pitha("Chitoi pitha", "Multi-test")
# print(chitoi)
print("Name: ", chitoi.name)
print("Taste: ", chitoi.taste)

chitoi.taste_is() # Method

# Object/instance: vapa
vapa = Pitha("vapa", "sweet")
print("Name: ", chitoi.name)
print("Taste: ", chitoi.taste)
vapa.taste_is()

