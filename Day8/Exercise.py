class Car:
    def __init__(self, color, seat):
        self.color = color
        self.seat = seat


class Brand:
    def __init__(self, name):
        self.name = name

cars = [
    Car("Red", "Seven"),
    Car("Red", "Four"),
    Car("Blue", "Seven"),
    Car("Blue", "Four")
]

print("\nAvailable Car Options")
print("Color\tSeat")
for car in cars:
    print(f"{car.color}\t{car.seat}")

def choose_car():
    input_color = input("\nChoose Color: ")
    input_seat = input("Choose Seat: ")

    for car in cars:
        if car.color == input_color and car.seat == input_seat:
            print(f"\nYou selected: {car.color} color, {car.seat} seats")
            return car 

    print("No matching car found!")
    return None


selected_car = choose_car()

if selected_car: 

    brands = [
        Brand("Toyota"),
        Brand("Mercedes"),
        Brand("Audi"),
        Brand("Porsche")
    ]

    print("\nAvailable Brands:")
    for brand in brands:
        print(brand.name)

    chosen_brand = input("Choose Brand: ")

    found_brand = None
    for brand in brands:
        if brand.name == chosen_brand:
            found_brand = brand
            break

    if found_brand:
        print(f"\nFinal Selection:")
        print(f"Color: {selected_car.color}")
        print(f"Seat:  {selected_car.seat}")
        print(f"Brand: {found_brand.name}")
    else:
        print("\nBrand not found!")
