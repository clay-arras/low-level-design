from ctypes import ArgumentError
from typing import Self

from clock import Clock
from fee_strategy import FeeStrategy
from floor import Floor
from parking_spot import ParkingSpot
from parking_strategy import ParkingStrategy
from vehicle import Vehicle


class ParkingLot:
    _instance = None

    def __new__(cls, *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(
        self,
        floors: list[Floor],
        parking_strat: ParkingStrategy,
        fee_strat: FeeStrategy,
        clock: Clock,
    ) -> None:
        if hasattr(self, "is_initialized") and self.is_initialized:
            return
        self.is_initialized = True

        self.floors = floors
        self.parking_index = {}
        self.start_time = {}

        self.parking_strategy = parking_strat
        self.fee_strategy = fee_strat

        self.clock = clock
        self.max_capacity = sum([len(floor.spots) for floor in self.floors])

    def park_vehicle(self, new_vehicle: Vehicle) -> ParkingSpot:
        if new_vehicle.uid in self.parking_index.keys():
            raise ArgumentError("Vehicle in parking lot")

        selected_spot = self.parking_strategy.park_vehicle(
            floors=self.floors, new_vehicle=new_vehicle
        )
        if selected_spot is None:
            raise Exception("Parking lot is full")

        selected_spot.vehicle = new_vehicle
        self.parking_index[new_vehicle.uid] = selected_spot
        self.start_time[new_vehicle.uid] = self.clock.get_time()
        return selected_spot

    def unpark_vehicle(self, parked_vehicle: Vehicle) -> None:
        if parked_vehicle.uid not in self.parking_index.keys():
            raise ArgumentError("Vehicle not in parking lot")
        self.parking_index[parked_vehicle.uid].vehicle = None
        del self.parking_index[parked_vehicle.uid]

        start_time = self.start_time[parked_vehicle.uid]
        end_time = self.clock.get_time()
        del self.start_time[parked_vehicle.uid]

        return self.fee_strategy.get_fee(start_time, end_time, parked_vehicle)

    def is_full(self) -> bool:
        return len(self.parking_index.items()) == self.max_capacity
