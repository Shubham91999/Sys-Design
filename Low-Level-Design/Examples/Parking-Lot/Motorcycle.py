from VehicleType import VehicleType
from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.MOTORCYCLE)