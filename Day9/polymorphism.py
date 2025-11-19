class vehicle:
    def __init__(self, name, move):
        self.name = name # public
        # self._move = move # protected
        self.move = move # private
    
    def __repr__(self):
        return f"{self.name} vehicle {self.move}"
    
car = vehicle("car", "runs")
print(car)
# inheritance
class flying_vehicle(vehicle):
    # polymorphism
    def __init__(self, name, move, rotor_type):
        super().__init__(name, move) # Parent theke inherit kortechi, ba access kortechi
        self.rotor_type = rotor_type

    def __repr__(self):
        return f"{self.name} Aircraft {self.move}, it has {self.rotor_type} fan rotor"

class flying_vehecle2(flying_vehicle):
    def __init__(self, name, move, rotor_type, seat):
        super().__init__(name, move, rotor_type) # Parent theke inherit kortechi, ba access kortechi
        self.seat = seat

    def __repr__(self):
        return f"{self.name} Aircraft {self.move}, it has {self.rotor_type} fan rotor and it has {self.seat} seat only"
    
cargo_plane = flying_vehecle2("cargo plane", "fly", "turbo", "four")
print(cargo_plane)
