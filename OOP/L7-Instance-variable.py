class Car:
    def __init__(self, name, model):
        self.name = name
        self.model_year = model
        self.wheel = 4

    def view(self):
        print("model")

#===========================

c1 = Car("Toyota", 2016)

c1.view()