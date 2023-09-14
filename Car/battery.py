from datetime import date


class Battery:
    def needs_service(self) -> bool:
        pass


class SpindlerBattery(Battery):
    def __init__(self, current_date: date, last_service_date: date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        years = (self.current_date - self.last_service_date).days / 365.0
        return years > 2


class NubbinBattery(Battery):
    def __init__(self, current_date: date, last_service_date: date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        years = (self.current_date - self.last_service_date).days / 365.0
        return years > 4
