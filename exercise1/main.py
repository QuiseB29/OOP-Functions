class Vehicle:
    def __init__(self,registration_number,vehicle_type,owner):
        self.registration_number = registration_number
        self.vehicle_type = vehicle_type
        self.owner = owner
        
    def update_owner(self, new_owner ):
        self.owner = new_owner 
        
    def display_details(self):
        print(f"Registration: {self.registration_number}, Type: {self.vehicle_type}, Owner: {self.owner}")
vehicles = {}

def register_vehicle(registration_number,vehicle_type,owner):
    if registration_number in vehicles:
        print("Error:Registration number already exists.")
        return
    vehicles[registration_number] = Vehicle(registration_number,vehicle_type,owner)
    print(f"Vehicle with reg num {registration_number} registered.") 
    
def update_vehicle_owner(registration_number,new_owner):
    if registration_number in vehicles:
        vehicles[registration_number].update_owner(new_owner)
        print(f"Updated owner for {registration_number}.")
    else:
        print("Vehicle not found.")
        
def display_all_vehicles():
    for vehicle in vehicles.values():
        vehicle.display_details()
        
while True:
    action = input("Enter action (register, update, display, exit):").lower()
    if action == "exit":
        break
    
    try:
        if action == "register":
            registration_number = input("Enter registration number:")
            vehicle_type = input("Enter vehicle type:")
            owner = input("Enter Owner Name:")
            register_vehicle(registration_number,vehicle_type,owner)
        elif action == "update":
            registration_number = input("Enter registration number:")
            new_owner = input("Enter new owner name:")
            update_vehicle_owner(registration_number,new_owner)
        elif action == "display":
            display_all_vehicles()
    except Exception as e:
        print(f"An Error occured: {e}")
        
print("DMV System Cloud")