from VehicleType import VehicleType
from Vehicle import Vehicle

class ParkingSpot:

    # Constructor will uniquely identify the parking spot with spot_number, defaulting vehicle type to CAR which can be changed later and parked_vehicle as None states, spot is empty right now
    def __init__(self, spot_number: int):
        self.spot_number = spot_number
        self.vehicle_type = VehicleType.CAR  # Setting default vehicle type to CAR
        self.parked_vehicle = None
        
    # Function to check of the parking spot is available, returns True if nothing's parked, false otherwise
    def is_available(self) -> bool:
        # return self.parked_vehicle is None
        if not self.parked_vehicle:
            return True
        else:
            return False
    
    # Function checks is spot is available and on success assigns Vehicle object to self.parked_vehicle
    def park_vehicle(self, vehicle: Vehicle) -> None:
        if self.is_available() and vehicle.get_type() == self.vehicle_type:
            self.parked_vehicle = vehicle
        else:
            raise ValueError("Invalid vehicle type or spot is already occupied.")
        
    # Function to set spot to available by setting self.parked_vehicle to None
    def unpark_vehicle(self) -> None:
        self.parked_vehicle = None

    # Tells users what kind of vehicle this spot accepts
    def get_vehicle_type(self) -> VehicleType:
        return self.vehicle_type
    
    # Returns type of vehicle currently parked at the spot
    def get_parked_vehicle(self) -> Vehicle:
        return self.parked_vehicle
    
    # Returns the spot identifier
    def get_spot_number(self) -> int:
        return self.spot_number
    

    # Encapsulation is achieved with park_vehicle() and unpark_vehicle() methds: Not allowing to manipulate parked_vehicle directly

    # Type Safety: Enforces at runtime that you only park the right kind of vehicle in each spot

    # is_available() and getter methods give all the required information to build higher-level components like Level and ParkingSpot classes

