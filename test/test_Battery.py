import unittest
from datetime import date
from Car.battery import NubbinBattery, SpindlerBattery


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year-4)
        nubbin = NubbinBattery(current_date, last_service_date)
        self.assertTrue(nubbin.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year-1)
        nubbin = NubbinBattery(current_date, last_service_date)
        self.assertFalse(nubbin.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year-3)
        nubbin = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(nubbin.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year-1)
        nubbin = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(nubbin.needs_service())
