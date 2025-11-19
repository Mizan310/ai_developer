class vehicle:
    def __init__(self, name, move):
        self.name = name # public
        # self._move = move # protected
        self.__move = move # private
    
    def __repr__(self):
        return f"{self.name} vehicle {self.__move}"
    
car = vehicle("car", "runs")
# print(car)
# print(car.move)
print(car.__move)