# Magic method
class Pitha:
    def __init__(self, name, taste):
        # print(name, taste)
        self.name = name
        self.taste = taste
    # Method
    # def taste_is(self):
    #     x = self.taste
    #     print(f"{self.name} pitha has {x}")
    
    def __repr__(self):
        return f"{self.name} pitha has {self.taste}"
 
    # pass

# Object/instance: chitoi
chitoi = Pitha("Chitoi pitha", "Multi-test")
# print(chitoi)
print("Name: ", chitoi.name)
print("Taste: ", chitoi.taste)
print(chitoi)

# chitoi.taste_is() # Method

# Object/instance: vapa
vapa = Pitha("vapa", "sweet")
print("Name: ", chitoi.name)
print("Taste: ", chitoi.taste)
# vapa.taste_is()
print(vapa)