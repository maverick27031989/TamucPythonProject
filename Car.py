class Car:

    max_miles = 0

    def __init__(self, efficiency):
        self.efficiency = efficiency

    def drive(self, distance):
        if self.max_miles < distance:
            return 0
        else:
            self.max_miles -= distance
            return 1

    def get_gas_level(self):
        return self.max_miles/self.efficiency

    def add_gas(self, fuel):
        self.max_miles += fuel*self.efficiency

