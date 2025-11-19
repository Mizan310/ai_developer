class Pitha:
    def __init__(self, name, taste):
        # print(name, taste)
        self.name = name
        self.taste = taste
    # Method
    def __repr__(self):
        return f"{self.name} has {self.taste}. So we have to tast it"

# Object/instance: chitoi
chitoi = Pitha("Chitoi", "Multi-taste")
print(chitoi)

# Inherit
class different_pitha(Pitha):
    def __init__(self, name, taste, quantity):
        super().__init__(name, taste)
        self.quantity = quantity
    def __repr__(self):
        return f"{self.name} has {self.taste}. So we have to tast it {self.quantity} pices"
vapa_pitha = different_pitha("Vapa", "Sweet", "20")
print(vapa_pitha)

class another_pitha(different_pitha):
    def __init__(self, name, taste, quantity, extra):
        super().__init__(name, taste, quantity)
        self.extra = extra
    def __repr__(self):
        return f"{self.name} has {self.taste}. So we have to tast it {self.quantity} pices. And give me extra {self.extra} pices"
vapa_pitha = another_pitha("Vapa", "Sweet", "20", "5")
print(vapa_pitha)