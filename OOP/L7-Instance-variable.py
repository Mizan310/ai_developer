class Car:
    def __init__(self, name, model):
        self.name = name
        self.model_year = model
        self.wheel = 4

    def view(self): # instance method
        print("The model year of this", self.name, "is", self.model_year)
        print("It is a", self.wheel, "wheel car")

#===========================

c1 = Car("Toyota", 2016)
c2 = Car("Audi", 2012)
c1.view()
c2.wheel = 6
c2.view()