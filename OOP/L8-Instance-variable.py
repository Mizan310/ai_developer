# __dict__

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def updateColor(self, color):
        self.color = color

    def poke(self):
        print(self.color, self.name, "is smiling")

dog = Dog("Rover", "Brown")
dog2 = Dog("Tomy", "White")
dog.poke()
dog2.poke()