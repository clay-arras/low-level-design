from abc import ABC, abstractmethod
from dataclasses import dataclass
from floor import Floor
from parking_spot import ParkingSpot
from vehicle import Vehicle


@dataclass
class ParkingStrategy(ABC):
    @abstractmethod
    def park_vehicle(
        self, floors: list[Floor], new_vehicle: Vehicle
    ) -> ParkingSpot | None:
        pass


class FirstAvailableParkingStrategy(ParkingStrategy):
    def park_vehicle(
        self, floors: list[Floor], new_vehicle: Vehicle
    ) -> ParkingSpot | None:
        for floor in floors:
            for spot in floor.spots:
                if spot.vehicle is None and spot.size >= new_vehicle.min_parking_size:
                    return spot
        return None


class TightestFitParkingStrategy(ParkingStrategy):
    def sort_floors(self, floors: list[Floor]) -> dict[int, list[ParkingSpot]]:
        order = {}
        for floor in floors:
            order[floor.level] = sorted(
                enumerate(floor.spots), key=lambda x: x[1].size.value
            )
        return order

    def park_vehicle(
        self, floors: list[Floor], new_vehicle: Vehicle
    ) -> ParkingSpot | None:
        order = self.sort_floors(floors)
        for floor in floors:
            for _, spot in order[floor.level]:
                if spot.vehicle is None and spot.size >= new_vehicle.min_parking_size:
                    return spot
        return None
