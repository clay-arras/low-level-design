from dataclasses import dataclass
from parking_spot_size import ParkingSpotSize
from vehicle import Vehicle


@dataclass
class ParkingSpot:
    uid: int
    size: ParkingSpotSize
    vehicle: Vehicle | None
