from abc import ABC, abstractmethod

# =========================
# VEHICLE BASE CLASS
# =========================
class Vehicle(ABC):
    def __init__(self, color, seat, price):
        self._color = color
        self._seat = seat
        self._price = float(price)

    @abstractmethod
    def description(self):
        pass

    def get_color(self):
        return self._color

    def get_seat(self):
        return self._seat

    def get_price(self):
        return self._price


# =========================
# CAR CLASS
# =========================
class Car(Vehicle):
    def __init__(self, color, seat, price, brand, model):
        super().__init__(color, seat, price)
        self._brand = brand
        self._model = model

    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model

    def description(self):
        return f"{self._brand} {self._model} | Color: {self._color}, Seats: {self._seat}, Price: ${self._price}"


# =========================
# BRAND CLASS
# =========================
class Brand:
    def __init__(self, name):
        self.name = name


# =========================
# CUSTOMER CLASS
# =========================
class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, car):
        self.cart.append(car)

    def get_total_bill(self):
        return sum(car.get_price() for car in self.cart)

    def generate_receipt(self):
        print("\n========== RECEIPT ==========")
        print(f"Customer: {self.name}\n")

        for car in self.cart:
            print(f"{car.get_brand()} {car.get_model()} - ${car.get_price()}")

        print("-----------------------------")
        print(f"Total Bill: ${self.get_total_bill()}")
        print("==============================\n")


# =========================
# CAR STORE
# =========================
class CarStore:
    def __init__(self):
        self.cars = []
        self.brands = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)

    def add_brand(self, brand):
        self.brands.append(brand)

    def show_cars(self):
        if not self.cars:
            print("\nNo cars available in stock!\n")
            return

        print("\nAvailable Cars:")
        print("Brand | Model | Color | Seat | Price")
        print("--------------------------------------------")
        for car in self.cars:
            print(f"{car.get_brand()} | {car.get_model()} | {car.get_color()} | {car.get_seat()} | ${car.get_price()}")
        print()

    def choose_car(self, color, seat):
        for car in self.cars:
            if car.get_color() == color and car.get_seat() == seat:
                return car
        return None


# =========================
# MAIN PROGRAM LOOP
# =========================
store = CarStore()

# Pre-loaded brands
store.add_brand(Brand("Toyota"))
store.add_brand(Brand("Audi"))
store.add_brand(Brand("Mercedes"))
store.add_brand(Brand("Porsche"))

# Pre-loaded cars
store.add_car(Car("Red", "Four", 20000, "Toyota", "Corolla"))
store.add_car(Car("Red", "Seven", 55000, "Audi", "Q7"))
store.add_car(Car("Blue", "Four", 42000, "Mercedes", "C-Class"))
store.add_car(Car("Blue", "Seven", 75000, "Porsche", "Cayenne"))

# PROGRAM RUNS FOREVER UNTIL EXIT
while True:

    print("\n========= CAR STORE MENU =========")
    print("1. Buy a Car")
    print("2. Add New Car (Admin)")
    print("3. Show Cars")
    print("4. Exit")
    print("===================================")

    choice = input("Choose an option: ")

    # OPTION 3: SHOW CARS
    if choice == "3":
        store.show_cars()

    # OPTION 2: ADD NEW CAR
    elif choice == "2":
        print("\n--- Add New Car ---")
        brand = input("Brand: ")
        model = input("Model: ")
        color = input("Color: ")
        seat = input("Seat (Four/Seven): ")
        price = float(input("Price: "))

        store.add_car(Car(color, seat, price, brand, model))
        print("\nCar added successfully!")

    # OPTION 1: BUY A CAR
    elif choice == "1":
        store.show_cars()
        name = input("Enter your name: ")
        customer = Customer(name)

        color = input("Choose Color: ")
        seat = input("Choose Seat: ")

        selected = store.choose_car(color, seat)

        if selected:
            print("\nYou selected:")
            print(selected.description())

            customer.add_to_cart(selected)
            store.remove_car(selected)

            customer.generate_receipt()

            print("\nUpdated Car List:")
            store.show_cars()

        else:
            print("\nNo matching car found!")

    # ❌ EXIT PROGRAM
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
