class ApartmentBuilding:
    def __init__(self, name, total_floors):
        self.name = name
        self.total_floors = total_floors
        self.occupied_floors = 0

    def update_floors(self, change):
        new_occupied = self.occupied_floors + change
        if 0 <= new_occupied <= self.total_floors:
            self.occupied_floors = new_occupied
            return True
        return False

    def available_units(self):
        return self.total_floors - self.occupied_floors

    def occupancy_rate(self):
        return (self.occupied_floors / self.total_floors) * 100
    
    @staticmethod
    def save_buildings_to_file(buildings, filename):
        with open(filename, 'w') as file:
            for building in buildings:
                file.write(f"{building.name}, {building.total_floors}\n")


buildings = []

while True:
    action = input("Enter action (add, update, display, save, exit): ").lower()
    if action == "exit":
        break

    try:
        if action == "add":
            name = input("Enter building name: ")
            floors = int(input("Enter total floors: "))
            buildings.append(ApartmentBuilding(name, floors))
            print(f"Building '{name}' added with {floors} floors.")
        elif action == "update":
            name = input("Enter building name to update floors: ")
            change = int(input("Enter change in building floors: "))
            for building in buildings:
                if building.name == name:
                    if building.update_floors(change):
                        print(f"Updated floors for '{name}'.")
                    else:
                        print("Invalid floor change. Ensure floors remain within the building's capacity.")
                    break
            else:
                print("Building not found.")
        elif action == "display":
            for building in buildings:
                print(f"{building.name}: {building.available_units()} total floors, "
                      f"Occupancy rate: {building.occupancy_rate():.2f}%")
        elif action == "save":
            filename = input("Enter filename to save: ")
            ApartmentBuilding.save_buildings_to_file(buildings, filename)
            print("Buildings saved to file.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for floors.")
    except Exception as e:
        print(f"An error occurred: {e}")
        

        
