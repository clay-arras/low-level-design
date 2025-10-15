from vehicle import Vehicle
from parking_spot_size import ParkingSpotSize


class Truck(Vehicle):
    def __init__(self, uid: str) -> None:
        super().__init__(uid)

    @property
    @classmethod
    def min_parking_size(cls) -> ParkingSpotSize:
        return ParkingSpotSize.LARGE
