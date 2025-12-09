class House:
    def __init__(self):
        self.window = 4 # instance variable
        self.door = 2 # instance variable

    def details(self):
        print(self.window, "windows", self.door, "doors")

h1 = House()
h2 = House()

# House.details(h1)
h1.details()
h2.details()

h1.window = 6
h2.door = 3

h1.details()
h2.details()