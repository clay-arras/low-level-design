from dataclasses import dataclass

from parking_spot import ParkingSpot


@dataclass
class Floor:
    level: int
    spots: list[ParkingSpot]
