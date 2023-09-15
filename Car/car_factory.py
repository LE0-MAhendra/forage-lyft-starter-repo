from battery import *
from engine import *
from car import Car
from tire import *


class CarFactory:
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list[float]) -> Car:
        calliope_engine = CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        calliope_battery = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date)
        tire = CarriganTire(tire_wear=tire_wear)
        return Car(engine=calliope_engine, battery=calliope_battery, tire=tire)

    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list[float]) -> Car:
        glissade_engine = WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        glissade_battery = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date)
        tire = OctoprimeTire(tire_wear=tire_wear)
        return Car(engine=glissade_engine, battery=glissade_battery, tire=tire)

    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool, tire_wear: list[float]) -> Car:
        palindrome_engine = SternmanEngine(
            warning_light_is_on=warning_light_on)
        palindrome_battery = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date)
        tire = CarriganTire(tire_wear=tire_wear)
        return Car(engine=palindrome_engine, battery=palindrome_battery, tire=tire)

    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list[float]) -> Car:
        rorschach_engine = WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        rorschach_battery = NubbinBattery(
            current_date=current_date, last_service_date=last_service_date)
        tire = OctoprimeTire(tire_wear=tire_wear)
        return Car(engine=rorschach_engine, battery=rorschach_battery, tire=tire)

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list[float]) -> Car:
        thovex_engine = CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        thovex_battery = NubbinBattery(
            current_date=current_date, last_service_date=last_service_date)
        tire = CarriganTire(tire_wear=tire_wear)
        return Car(engine=thovex_engine, battery=thovex_battery, tire=tire)
