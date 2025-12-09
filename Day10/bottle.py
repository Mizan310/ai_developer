class Bottle:
    def __init__(self, volume, color, material, status):
        self.volume = volume
        self.color = color
        self.material = material
        self.status = status
    
    def fill_up(self):
        print("The botlle is full now")

    def empty(self):
        print("The bottle is empty")

    def __repr__(self):
        return f"the bottle is {self.color}, And it is {self.status}"

# bottle = Bottle("1L", "Transparent", "Plastic", "empty")

# print(bottle.volume, bottle.color, bottle.material)
# print(bottle)

'''
create a child class based on Bottle class.
materialized the methods in the parent Bottle class
if you need to change any ethod or attribute of the parent class
    you are free to do so

'''

class waterBottle(Bottle):
    def __init__(self, volume, color, material, status):
        super().__init__(volume, color, material, status)
    
    def fill_up(self):
        # return f"{self.color}"
        print("The bottle is filling up...")
        self.status = "halfffffff"

    def empty(self):
        print("The bottle is empty now...")
        self.status = "emptyyy"
    
    def __repr__(self):
        return f"the bottle is {self.color}, And it is {self.status}"
    
newBottle = waterBottle("1.5L", "Transparent", "Plastic", "emptyy")
print(newBottle)
newBottle.fill_up()
# print("Status is", newBottle)
newBottle.empty()
# print("Status is: ", newBottle)