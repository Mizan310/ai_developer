from abc import ABC, abstractmethod

# =========================
# VEHICLE BASE CLASS
# =========================
class Vehicle(ABC):
    def __init__(self, color, seat, price, quantity=1):
        self._color = color
        self._seat = seat
        self._price = float(price)
        self._quantity = quantity

    @abstractmethod
    def description(self):
        pass

    def get_color(self):
        return self._color

    def get_seat(self):
        return self._seat

    def get_price(self):
        return self._price

    def get_quantity(self):
        return self._quantity

    def increase_quantity(self, amount=1):
        self._quantity += amount

    def decrease_quantity(self, amount=1):
        self._quantity -= amount


# =========================
# CAR CLASS
# =========================
class Car(Vehicle):
    def __init__(self, color, seat, price, brand, model, quantity=1):
        super().__init__(color, seat, price, quantity)
        self._brand = brand
        self._model = model

    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model

    def description(self):
        return (f"{self._brand} {self._model} | Color: {self._color}, "
                f"Seats: {self._seat}, Price: ${self._price}, Quantity: {self._quantity}")


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

    def add_brand(self, brand):
        self.brands.append(brand)

    # FIND IF SAME CAR ALREADY EXISTS
    def find_existing_car(self, brand, model, color, seat, price):
        for car in self.cars:
            if (car.get_brand() == brand and 
                car.get_model() == model and 
                car.get_color() == color and 
                car.get_seat() == seat and 
                car.get_price() == float(price)):
                return car
        return None

    def add_car(self, car):
        # if same car exists → increase quantity instead of adding new row
        existing = self.find_existing_car(car.get_brand(), car.get_model(), 
                                          car.get_color(), car.get_seat(), car.get_price())
        if existing:
            existing.increase_quantity(car.get_quantity())
        else:
            self.cars.append(car)

    def show_cars(self):
        if not self.cars:
            print("\nNo cars available in stock!\n")
            return

        print("\nAvailable Cars:")
        print("Brand | Model | Color | Seat | Price | Quantity")
        print("-------------------------------------------------------")
        for car in self.cars:
            print(f"{car.get_brand()} | {car.get_model()} | {car.get_color()} | "
                  f"{car.get_seat()} | ${car.get_price()} | {car.get_quantity()}")
        print()

    def choose_car(self, color, seat):
        for car in self.cars:
            if car.get_color() == color and car.get_seat() == seat and car.get_quantity() > 0:
                return car
        return None

    def decrease_stock(self, car):
        car.decrease_quantity()
        if car.get_quantity() <= 0:
            self.cars.remove(car)


# =========================
# MAIN PROGRAM LOOP
# =========================
store = CarStore()

# Pre-loaded brands
store.add_brand(Brand("Toyota"))
store.add_brand(Brand("Audi"))
store.add_brand(Brand("Mercedes"))
store.add_brand(Brand("Porsche"))

# Pre-loaded cars with quantity
store.add_car(Car("Red", "Four", 20000, "Toyota", "Corolla", quantity=2))
store.add_car(Car("Red", "Seven", 55000, "Audi", "Q7", quantity=3))
store.add_car(Car("Blue", "Four", 42000, "Mercedes", "C-Class", quantity=1))
store.add_car(Car("Blue", "Seven", 75000, "Porsche", "Cayenne", quantity=2))

# PROGRAM MENU LOOP
while True:

    print("\n========= CAR STORE MENU =========")
    print("1. Buy a Car")
    print("2. Add New Car (Admin)")
    print("3. Show Cars")
    print("4. Exit")
    print("===================================")

    choice = input("Choose an option: ")

    # SHOW CARS
    if choice == "3":
        store.show_cars()

    # ADD NEW CAR
    elif choice == "2":
        print("\n--- Add New Car ---")
        brand = input("Brand: ")
        model = input("Model: ")
        color = input("Color: ")
        seat = input("Seat (Four/Seven): ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        store.add_car(Car(color, seat, price, brand, model, quantity))
        print("\nCar added successfully!")

    # BUY CAR
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
            store.decrease_stock(selected)

            customer.generate_receipt()

            print("\nUpdated Car List:")
            store.show_cars()
        else:
            print("\nNo matching car found or out of stock!")

    # EXIT
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
