from parking_spot_size import ParkingSpotSize
from vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, uid: str) -> None:
        super().__init__(uid)

    @property
    @classmethod
    def min_parking_size(cls) -> ParkingSpotSize:
        return ParkingSpotSize.SMALL
