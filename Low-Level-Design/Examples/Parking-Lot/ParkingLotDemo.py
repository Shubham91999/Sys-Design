from ParkingLot import ParkingLot
from Level import Level
from Car import Car
from Motorcycle import Motorcycle
from Truck import Truck

class ParkingLotDemo:

    def run():
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_level(Level(1, 100))
        parking_lot.add_level(Level(2, 80))


        car = Car("ABCXYZ")
        motorcycle = Motorcycle("SJADSD")
        truck = Truck("NJNJ")

        # Park Vehicles
        parking_lot.park_vehicle(car)
        parking_lot.park_vehicle(motorcycle)
        parking_lot.park_vehicle(truck)

        # Display Availability
        parking_lot.display_availability()

        # Unpark vehicle
        parking_lot.unpark_vehicle(motorcycle)

        # Display Updated Availability
        parking_lot.display_availability()

if __name__ == "__main__":
    ParkingLotDemo.run()