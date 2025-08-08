from enum import Enum
from abc import ABC
from typing import List, Optional
import threading
from datetime import datetime


class VehicleType(Enum):
    CAR = 1
    BIKE = 2
    TRUCK = 3

class Vehicle(ABC):
    def __init__(self, licensePlate: str, vehicleType: VehicleType):
        self.licensePlate = licensePlate
        self.type = vehicleType

    def getType(self):
        return self.type

class Car(Vehicle):
    def __init__(self, licensePlate: str):
        super().__init__(licensePlate, VehicleType.CAR)

class Bike(Vehicle):
    def __init__(self, licensePlate: str):
        super().__init__(licensePlate, VehicleType.BIKE)

class Truck(Vehicle):
    def __init__(self, licensePlate: str):
        super().__init__(licensePlate, VehicleType.TRUCK)

class ParkingSpot:
    def __init__(self, spotNumber: int, vehicleType: VehicleType):
        self.spotNumber = spotNumber
        self.vehicleType = vehicleType
        self.parkedVehicle = None

    def isAvailable(self) -> bool:
        return self.parkedVehicle is None
    
    def parkVehicle(self, vehicle: Vehicle) -> None:
        if self.isAvailable() and vehicle.getType() == self.vehicleType:
            self.parkedVehicle = vehicle
        else:
            raise ValueError("Invalid vehicle type or spot already occupied")
        
    def unparkVehicle(self) -> None:
        if self.parkedVehicle:
            self.parkedVehicle = None
        else:
            raise ValueError("Spot is already unoccupied")
        
    def getVehicleType(self) -> VehicleType:
        return self.vehicleType
    
    def getParkedVehicle(self) -> Optional[Vehicle]:
        return self.parkedVehicle
    
    def getSpotNumber(self) -> int:
        return self.spotNumber
        
class Level:
    def __init__(self, floor: int, numSpots: int):
        self.floor = floor
        self.parkingSpots: List[ParkingSpot] = []
        for i in range(numSpots):
            if i % 3 == 0:
                self.parkingSpots.append(ParkingSpot(i, VehicleType.TRUCK))
            elif i % 3 == 1:
                self.parkingSpots.append(ParkingSpot(i, VehicleType.CAR))
            elif i % 3 == 2:
                self.parkingSpots.append(ParkingSpot(i, VehicleType.BIKE))


    def display_availability(self) -> None:
        print(f"Level {self.floor} Availability:")
        for spot in self.parkingSpots:
            print(f"Spot {spot.getSpotNumber()} is {'Available' if spot.isAvailable() else 'Occupied'}")
        
    def parkVehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parkingSpots:
            if spot.isAvailable() and spot.getVehicleType() == vehicle.getType():
                spot.parkVehicle(vehicle)
                return True
        return False
    
    def unparkVehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parkingSpots:
            if not spot.isAvailable() and spot.getParkedVehicle() == vehicle:
                spot.unparkVehicle()
                return True
        return False
    
class Ticket:
    def __init__(self, ticketId: int, vehicle: Vehicle, spot: ParkingSpot, issueTime: datetime):
        self.ticketId = ticketId
        self.vehicle = vehicle
        self.spot = spot
        self.issueTime = issueTime

    def __str__(self):
        return f"Ticket#{self.ticketId} for {self.vehicle.licensePlate} at Spot {self.spot.getSpotNumber()} on Floor {self.spot.spotNumber // 100}"

    
class ParkingLot:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception('Already one instance is created')
        else:
            ParkingLot._instance = self
            self.levels: List[Level] = []
            self.ticketCounter = 1
            self.ticketMap = {}

    @staticmethod
    def getInstance():
        with ParkingLot._lock:
            if ParkingLot._instance is None:
                ParkingLot._instance = ParkingLot()
        return ParkingLot._instance
    
    def addLevel(self, level: Level) -> None:
        self.levels.append(level)

    def parkVehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.parkVehicle(vehicle):
                return True
        return False
    
    def unparkVehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.unparkVehicle(vehicle):
                return True
        return False
    
    def displayAvailability(self) -> None:
        for level in self.levels:
            level.display_availability()
            
    
class ParkingLotDemo:
    @staticmethod
    def run():
        parking_lot = ParkingLot.getInstance()
        parking_lot.addLevel(Level(1, 100))
        parking_lot.addLevel(Level(2, 80))

        car = Car("ABC123")
        truck = Truck("XYZ789")
        motorcycle = Bike("M1234")
        car1 = Car("ABC123")
        truck1 = Truck("XYZ789")
        motorcycle1 = Bike("M1234")

        parking_lot.parkVehicle(car)
        parking_lot.parkVehicle(truck)
        parking_lot.parkVehicle(motorcycle)

        parking_lot.parkVehicle(car1)
        parking_lot.parkVehicle(truck1)
        parking_lot.parkVehicle(motorcycle1)

        parking_lot.displayAvailability()

        parking_lot.unparkVehicle(motorcycle)

        parking_lot.displayAvailability()

if __name__=="__main__":
    ParkingLotDemo.run()





    
    



        
    
