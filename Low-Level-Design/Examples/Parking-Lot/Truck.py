from VehicleType import VehicleType
from Vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, VehicleType.Truck)