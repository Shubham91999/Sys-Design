from enum import Enum
from abc import ABC, abstractmethod
from typing import List, Optional
import threading
from datetime import datetime

# --- Vehicle Definitions ---
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

# --- Parking Spot ---
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

# --- Level ---
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

# --- Ticket ---
class Ticket:
    def __init__(self, ticketId: int, vehicle: Vehicle, spot: ParkingSpot, issueTime: datetime):
        self.ticketId = ticketId
        self.vehicle = vehicle
        self.spot = spot
        self.issueTime = issueTime

    def __str__(self):
        return f"Ticket#{self.ticketId} for {self.vehicle.licensePlate} at Spot {self.spot.getSpotNumber()}"

# --- Parking Strategy (Strategy Pattern) ---
class ParkingStrategy(ABC):
    @abstractmethod
    def find_spot(self, vehicle: Vehicle, levels: List[Level]) -> Optional[ParkingSpot]:
        pass

class FirstAvailableStrategy(ParkingStrategy):
    def find_spot(self, vehicle: Vehicle, levels: List[Level]) -> Optional[ParkingSpot]:
        for level in levels:
            for spot in level.parkingSpots:
                if spot.isAvailable() and spot.getVehicleType() == vehicle.getType():
                    return spot
        return None

# --- ParkingLot Singleton ---
class ParkingLot:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception('Already one instance is created')
        ParkingLot._instance = self
        self.levels: List[Level] = []
        self.ticketCounter = 1
        self.ticketMap = {}
        self.strategy: ParkingStrategy = FirstAvailableStrategy()  # default

    @staticmethod
    def getInstance():
        with ParkingLot._lock:
            if ParkingLot._instance is None:
                ParkingLot()
        return ParkingLot._instance

    def setStrategy(self, strategy: ParkingStrategy):
        self.strategy = strategy

    def addLevel(self, level: Level) -> None:
        self.levels.append(level)

    def parkVehicle(self, vehicle: Vehicle) -> bool:
        spot = self.strategy.find_spot(vehicle, self.levels)
        if spot:
            spot.parkVehicle(vehicle)
            ticket = Ticket(self.ticketCounter, vehicle, spot, datetime.now())
            self.ticketMap[vehicle.licensePlate] = ticket
            self.ticketCounter += 1
            print(f"Issued {ticket}")
            return True
        print(f"No spot found for {vehicle.licensePlate}")
        return False

    def unparkVehicle(self, vehicle: Vehicle) -> bool:
        ticket = self.ticketMap.get(vehicle.licensePlate)
        if not ticket:
            print(f"No ticket found for {vehicle.licensePlate}")
            return False
        spot = ticket.spot
        duration = (datetime.now() - ticket.issueTime).total_seconds() / 60
        price = max(1, round(duration * 0.5, 2))
        spot.unparkVehicle()
        del self.ticketMap[vehicle.licensePlate]
        print(f"{vehicle.licensePlate} unparked. Duration: {duration:.2f} min. Fee: ${price}")
        return True

    def displayAvailability(self) -> None:
        for level in self.levels:
            level.display_availability()

# --- Demo ---
class ParkingLotDemo:
    @staticmethod
    def run():
        parking_lot = ParkingLot.getInstance()
        parking_lot.addLevel(Level(1, 15))
        parking_lot.addLevel(Level(2, 15))

        parking_lot.setStrategy(FirstAvailableStrategy())  # Set strategy

        vehicles = [
            Car("CAR123"),
            Truck("TRK456"),
            Bike("BIK789"),
            Car("CAR999")
        ]

        for v in vehicles:
            parking_lot.parkVehicle(v)

        parking_lot.displayAvailability()

        parking_lot.unparkVehicle(vehicles[2])  # Unpark bike
        parking_lot.displayAvailability()

if __name__ == "__main__":
    ParkingLotDemo.run()
