from abc import abstractmethod
from dataclasses import dataclass
from parking_spot_size import ParkingSpotSize


@dataclass
class Vehicle:
    uid: str

    @property
    @abstractmethod
    @classmethod
    def min_parking_size(cls) -> ParkingSpotSize:
        pass
