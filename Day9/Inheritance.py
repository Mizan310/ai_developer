class vehicle:
    def __init__(self, name, move):
        self.name = name # public
        # self._move = move # protected
        self.__move = move # private
    
    def __repr__(self):
        return f"{self.name} vehicle {self.__move}"
    
car = vehicle("car", "runs")

# print(car.__move)

# inheritance
class flying_vehicle(vehicle):
    pass
cargo_plane = flying_vehicle("cargo plane", "fly")
print(cargo_plane)