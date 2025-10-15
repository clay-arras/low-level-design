
## stage 1: clarifying questions
does each floor have the same number of parking spots, or does it vary by floor? 
do we know which parking spots are what sizes? 
is it important to have an unique id for each parking spot, or do we treat all parking spots of the same sizes as the same?
is it safe to assume that the only sizes are small, medium, and large? 
is it safe to assume the only types of vehicles are motorcycles, cars, and trucks? if so, is it safe to assume motorcycles can fit in small spot and greater, cars in medium and greater, trucks only in large? 

can we assume we have a list of Floor objects, where each Floor contains a list of Parking Spots, where each Parking Spot has an Id and a size? 

**post stage-1 questions**:
- can we assume that we are given the id's for the parking spots? how about the ids for the cars, or should the system assign unique ids for the cars?

## stage 2: uml diagram 

<!-- class VehicleSize(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2 -->

class ParkingSpotSize(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2

class Vehicle:
    id: str

    @property
    @abstractmethod
    @classmethod
    def min_parking_size(cls) -> ParkingSpotSize:
        pass

class Motorcycle(Vehicle): 
    def min_parking_size(cls) -> ParkingSpotSize:
        return ParkingSpotSize.SMALL

class Car(Vehicle): 
    def min_parking_size(cls) -> ParkingSpotSize:
        return ParkingSpotSize.MEDIUM

class Truck(Vehicle): 
    def min_parking_size(cls) -> ParkingSpotSize:
        return ParkingSpotSize.LARGE

class ParkingLot:
    floors: list[Floor]

class Floor:
    spots: list[ParkingSpot]

class ParkingSpot:
    id: int
    size: ParkingSpotSize
    vehicle: Vehicle | None


## stage 3: implementing a verticle slice

features needed to support:

- park_vehicle
- unpark_vehicle
- is_full
