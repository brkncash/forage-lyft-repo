from car import Car

from engine import *

from battery import *


class CarFactory:

    def create_calliope(self, last_service_mileage, current_mileage, last_service_date, current_date):
        return Car(CapuletEngine(last_service_mileage, current_mileage),
                   SpindlerBattery(last_service_date, current_date))

    def create_glissade(self, last_service_mileage, current_mileage, last_service_date, current_date):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage),
                   SpindlerBattery(last_service_date, current_date))

    def create_palindrome(self, warning_light_is_on, last_service_date, current_date):
        return Car(SternmanEngine(warning_light_is_on),
                   SpindlerBattery(last_service_date, current_date))

    def create_rorschach(self, last_service_mileage, current_mileage, last_service_date, current_date):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage),
                   NubbinBattery(last_service_date, current_date))

    def create_thovex(self, last_service_mileage, current_mileage, last_service_date, current_date):
        return Car(CapuletEngine(last_service_mileage, current_mileage),
                   NubbinBattery(last_service_date, current_date))
