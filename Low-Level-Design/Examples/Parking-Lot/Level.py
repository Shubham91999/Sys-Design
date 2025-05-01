from typing import List
from ParkingSpot import ParkingSpot
from Vehicle import Vehicle

class Level:

    # Constructor with integer identifier floor and list of ParkingSpot objects, with size equals to num_spots
    def __init__(self, floor: int, num_spots: int):
        self.floor = floor
        self.parking_spots: List[ParkingSpot] = [ParkingSpot(i) for i in range(num_spots)]
        # or 
        # self.parking_spots = List[ParkingSpot] = []
        # for i in range(num_spots):
        #     spot = ParkingSpot(i)
        #     self.parking_spots.append(spot)

    # Park in available spot on current level
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if spot.is_available() and spot.get_vehicle_type() == vehicle.get_type():
                spot.park_vehicle(vehicle)
                return True
        return False
    
    # Remove vehicle from whichever spot it's in 
    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if not spot.is_available() and spot.get_vehicle_type() == vehicle:
                spot.unpark_vehicle()
                return True
        return False
    
    # Displays the status of parking spots on current level
    def display_availability(self) -> None:
        print(f"Level {self.floor} Availability:")
        for spot in self.parking_spots:
            status = "Available" if spot.is_available() else "Occupied"
            print(f"Spot {spot.get_spot_number}: {status}")



        
