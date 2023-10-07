from abc import ABC

from tires import Tires


class Octoprime(Tires, ABC):

    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        if (self.tire_wear[0] + self.tire_wear[1] + self.tire_wear[2] + self.tire_wear[3]) >= 3:
            return True
        return False
