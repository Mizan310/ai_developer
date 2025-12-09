class vehicle:
    def __init__(self, name, move):
        self.name = name # public
        # self._move = move # protected
        self._move = move # private
    
    def __repr__(self):
        return f"{self.name} vehicle {self._move}"
    
car = vehicle("car", "runs")
# print(car)
# print(car.move)
print(car._move)
print(f"{car.name} {car._move} fast or slow, that based on engine")