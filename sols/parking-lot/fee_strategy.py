import datetime
from abc import ABC, abstractmethod
from math import ceil

from car import Car
from motorcycle import Motorcycle
from truck import Truck
from vehicle import Vehicle


class FeeStrategy(ABC):
    SECONDS_IN_HOUR: float = 60 * 60

    @abstractmethod
    def get_fee(
        self, start_time: datetime, end_time: datetime, vehicle: Vehicle
    ) -> float:
        pass


class FlatRateFeeStrategy(FeeStrategy):
    FLAT_RATE_FEE: float = 10

    def get_fee(
        self, start_time: datetime, end_time: datetime, vehicle: Vehicle
    ) -> float:
        diff = end_time - start_time
        return FlatRateFeeStrategy.FLAT_RATE_FEE * ceil(
            diff.total_seconds() / FeeStrategy.SECONDS_IN_HOUR
        )


class VehicleBasedFeeStrategy(FeeStrategy):
    VEHICLE_FEES = {
        Truck: 15,
        Car: 10,
        Motorcycle: 5,
    }  # using class names so refactoring is easier, less coupled

    def get_fee(
        self, start_time: datetime, end_time: datetime, vehicle: Vehicle
    ) -> float:
        diff = end_time - start_time
        fee = VehicleBasedFeeStrategy.VEHICLE_FEES[type(vehicle)]
        return fee * ceil(diff.total_seconds() / FeeStrategy.SECONDS_IN_HOUR)
