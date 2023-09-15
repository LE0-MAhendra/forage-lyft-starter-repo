from datetime import date
from abc import ABC, abstractmethod


class Tire(ABC):
    @abstractmethod
    def needs_service() -> bool:
        pass


class CarriganTire(Tire):
    def __init__(self, tire_wear: list[float]):
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        for value in self.tire_wear:
            if value >= 0.9:
                return True
        return False


class OctoprimeTire(Tire):
    def __init__(self, tire_wear: list[float]):
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        return sum(self.tire_wear) >= 3
