from dataclasses import dataclass
from parking_spot import ParkingSpot
from vehicle import Vehicle


@dataclass
class Floor:
    level: int
    spots: list[ParkingSpot]
