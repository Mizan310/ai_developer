from abc import ABC, abstractmethod

# =========================
# VEHICLE BASE CLASS
# =========================
class Vehicle(ABC):
    def __init__(self, category, price, quantity=1):
        self._category = category
        self._price = float(price)
        self._quantity = quantity
        self._cc = None

    @abstractmethod
    def description(self):
        pass

    def get_category(self):
        return self._category

    def get_price(self):
        return self._price

    def get_quantity(self):
        return self._quantity

    def increase_quantity(self, amount=1):
        self._quantity += amount

    def decrease_quantity(self, amount=1):
        self._quantity -= amount


# =============================
# PRIVATE CAR CLASS
# =============================
class PrivateCar(Vehicle):
    def __init__(self, brand, model, color, seat, price, quantity=1):
        super().__init__("Private Car", price, quantity)
        self._brand = brand
        self._model = model
        self._color = color
        self._seat = seat
        self._cc = self.assign_cc(seat)

    def assign_cc(self, seat):
        return {"4": 1200, "7": 1500, "10": 1800}.get(seat, 1200)

    def description(self):
        return (f"{self._brand} {self._model} | Color: {self._color}, Seats: {self._seat}, "
                f"CC: {self._cc}, Price: ${self._price}, Qty: {self._quantity}")


# =============================
# BUS CLASS
# =============================
class Bus(Vehicle):
    def __init__(self, company, seat, price, quantity=1):
        super().__init__("Bus", price, quantity)
        self._company = company
        self._seat = seat
        self._cc = self.assign_cc(seat)

    def assign_cc(self, seat):
        return {"40": 2000, "56": 3000}.get(seat, 2000)

    def description(self):
        return (f"{self._company} Bus | Seats: {self._seat}, CC: {self._cc}, "
                f"Price: ${self._price}, Qty: {self._quantity}")


# =============================
# TRUCK CLASS
# =============================
class Truck(Vehicle):
    def __init__(self, company, wheels, price, quantity=1):
        super().__init__("Truck", price, quantity)
        self._company = company
        self._wheels = wheels
        self._cc = self.assign_cc(wheels)

    def assign_cc(self, wheels):
        return {"6": 2500, "10": 4000, "12": 5000}.get(wheels, 2500)

    def description(self):
        return (f"{self._company} Truck | Wheels: {self._wheels}, CC: {self._cc}, "
                f"Price: ${self._price}, Qty: {self._quantity}")


# =========================
# CUSTOMER CLASS
# =========================
class Customer:
    def __init__(self, name, phone, address, nationality, item, qty, paid_amount):
        self.name = name
        self.phone = phone
        self.address = address
        self.nationality = nationality
        self.item = item
        self.qty = qty
        self.total_price = item.get_price() * qty
        self.paid = float(paid_amount)
        self.due = self.total_price - self.paid

    def receipt(self):
        print("\n========== RECEIPT ==========")
        print(f"Customer Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")
        print(f"Nationality: {self.nationality}")
        print("----------------------------------")
        print("Purchased Item:")
        print(f"{self.item.description()} (Purchased Qty: {self.qty})")
        print(f"Total Price: ${self.total_price}")
        print(f"Paid Amount: ${self.paid}")

        if self.due <= 0:
            print("Due: $0 (Full Paid)")
        else:
            print(f"Due: ${self.due}")

        print("==============================\n")


# =========================
# VEHICLE STORE
# =========================
class VehicleStore:
    def __init__(self):
        self.vehicles = []
        self.customers = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def show_category(self, category):
        filtered = [v for v in self.vehicles if v.get_category() == category]
        for i, v in enumerate(filtered, start=1):
            print(f"{i}. {v.description()}")
        return filtered

    def choose_vehicle(self, category, index):
        filtered = [v for v in self.vehicles if v.get_category() == category]
        if 1 <= index <= len(filtered):
            return filtered[index - 1]
        return None

    def decrease_stock(self, vehicle, amount):
        vehicle.decrease_quantity(amount)
        if vehicle.get_quantity() <= 0:
            self.vehicles.remove(vehicle)

    def show_all(self):
        print("\n===== All Vehicles =====")
        for v in self.vehicles:
            print(v.description())

    def show_customers(self):
        print("\n===== Customer List =====")

        if not self.customers:
            print("No customers yet.")
            return

        for i, c in enumerate(self.customers, start=1):
            print(f"{i}. Name: {c.name} | Phone: {c.phone} | Paid: ${c.paid} | Due: ${c.due} "
                    f"| Bought: {c.item.description()} | Purchased Qty: {c.qty}")

        print("\n1. Delete Customer")
        print("2. Go to Menu")

        option = input("Choose: ")

        if option == "1":
            idx = int(input("Enter customer number to delete: "))
            if 1 <= idx <= len(self.customers):
                del self.customers[idx - 1]
                print("Customer deleted successfully!")
            else:
                print("Invalid customer number.")


# =========================
# MAIN PROGRAM
# =========================
store = VehicleStore()

store.add_vehicle(PrivateCar("Toyota", "Corolla", "Red", "4", 18000, 3))
store.add_vehicle(PrivateCar("Audi", "Q7", "Black", "7", 55000, 2))
store.add_vehicle(Bus("Volvo", "56", 80000, 1))
store.add_vehicle(Truck("Tata", "10", 65000, 2))

ADMIN_PASSWORD = "admin123"

while True:
    print("\n========= VEHICLE STORE =========")
    print("1. Private Car")
    print("2. Bus")
    print("3. Truck")
    print("4. Add Vehicle (Admin)")
    print("5. Show Vehicles")
    print("6. Show Customer List (Admin)")
    print("7. Exit")
    print("==================================")

    choice = input("Choose an option: ")

    def buy_process(category):
        items = store.show_category(category)
        if not items: return

        idx = int(input("Select vehicle number: "))
        selected = store.choose_vehicle(category, idx)
        if not selected:
            print("Invalid selection!")
            return

        print(f"Available Quantity: {selected.get_quantity()}")
        qty = int(input("How many do you want to buy? "))

        if qty <= 0:
            print("Invalid quantity!")
            return

        if qty > selected.get_quantity():
            print("Not enough stock available!")
            return

        name = input("Customer Name: ")
        phone = input("Phone Number: ")
        address = input("Address: ")
        nationality = input("Nationality: ")
        paid_amount = float(input("Enter Paid Amount: "))

        customer = Customer(name, phone, address, nationality, selected, qty, paid_amount)
        store.customers.append(customer)
        store.decrease_stock(selected, qty)
        customer.receipt()

    if choice == "1": buy_process("Private Car")
    elif choice == "2": buy_process("Bus")
    elif choice == "3": buy_process("Truck")

    elif choice == "4":
        pwd = input("Enter admin password: ")
        if pwd != ADMIN_PASSWORD:
            print("Access denied!")
            continue

        print("\n--- Add Vehicle ---")
        print("1. Private Car\n2. Bus\n3. Truck")
        vtype = input("Choose type: ")

        if vtype == "1":
            brand = input("Brand: ")
            model = input("Model: ")
            color = input("Color: ")
            seat = input("Seat (4/7/10): ")
            price = float(input("Price: "))
            qty = int(input("Quantity: "))
            store.add_vehicle(PrivateCar(brand, model, color, seat, price, qty))

        elif vtype == "2":
            company = input("Company: ")
            seat = input("Seats (40/56): ")
            price = float(input("Price: "))
            qty = int(input("Quantity: "))
            store.add_vehicle(Bus(company, seat, price, qty))

        elif vtype == "3":
            company = input("Company: ")
            wheels = input("Wheels (6/10/12): ")
            price = float(input("Price: "))
            qty = int(input("Quantity: "))
            store.add_vehicle(Truck(company, wheels, price, qty))

        print("Vehicle Added Successfully!")

    elif choice == "5":
        store.show_all()

    elif choice == "6":
        pwd = input("Enter admin password: ")
        if pwd != ADMIN_PASSWORD:
            print("Access denied!")
            continue
        store.show_customers()

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
