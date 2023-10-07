from car import Car

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class CarFactory:

    def create_calliope(self, last_service_mileage, current_mileage, last_service_date, current_date, tire_wear):
        return Car(CapuletEngine(last_service_mileage, current_mileage),
                   SpindlerBattery(last_service_date, current_date),
                   CarriganTires(tire_wear))

    def create_glissade(self, last_service_mileage, current_mileage, last_service_date, current_date, tire_wear):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage),
                   SpindlerBattery(last_service_date, current_date),
                   CarriganTires(tire_wear))

    def create_palindrome(self, warning_light_is_on, last_service_date, current_date, tire_wear):
        return Car(SternmanEngine(warning_light_is_on),
                   SpindlerBattery(last_service_date, current_date),
                   OctoprimeTires(tire_wear))

    def create_rorschach(self, last_service_mileage, current_mileage, last_service_date, current_date, tire_wear):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage),
                   NubbinBattery(last_service_date, current_date),
                   OctoprimeTires(tire_wear))

    def create_thovex(self, last_service_mileage, current_mileage, last_service_date, current_date, tire_wear):
        return Car(CapuletEngine(last_service_mileage, current_mileage),
                   NubbinBattery(last_service_date, current_date),
                   OctoprimeTires(tire_wear))
