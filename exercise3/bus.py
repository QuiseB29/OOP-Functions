class Bus:
    def __init__(self, city, bus_fare, route, capacity):
        self.city = city
        self.bus_fare = bus_fare
        self.route_number = route
        self.capacity = capacity

    def add_city(self, change):
        self.city = change

    def update_bus_fare(self, new_fare):
        self.bus_fare = new_fare

    def update_route_number(self, new_route):
        self.route_number = new_route

    def update_capacity(self, new_capacity):
        self.capacity = new_capacity


bus_line = []

while True:
    action = input("Enter action (add, display, exit): ").lower()
    if action == "exit":
        break

    try:
        if action == "add":
            city = input("Enter city: ")
            bus_fare = float(input("Enter Bus Fare: "))
            route = int(input("Enter route number: "))
            capacity = int(input("Enter passenger capacity: "))
            bus = Bus(city, bus_fare, route, capacity)
            bus_line.append(bus)
        elif action == "display":
            for bus in bus_line:
                print(f"City: {bus.city}, Total fare: {bus.bus_fare}, Route Number: {bus.route_number}, Total People: {bus.capacity}")
    except ValueError:
        print("Invalid error. Please make numeric for Bus Fare and Capacity.")
    except Exception as e:
        print(f"An error occurred: {e}")
