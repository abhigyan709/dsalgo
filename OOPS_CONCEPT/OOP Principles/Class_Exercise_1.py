class Vehicle:
    def __init__(self):
        self.mileage = None
        self.fuel_left = None
    def identify_distance_travelled(self, initial_fuel):
        distance_travelled = (initial_fuel - self.fuel_left)*self.mileage
        return distance_travelled
    def identify_distance_that_can_be_travelled(self):
        initial_fuel = 15
        distance_travelled = self.identify_distance_travelled(initial_fuel)
        if self.fuel_left>5:
            return(initial_fuel-5)*self.mileage-distance_travelled
        else:
            return 0

car = Vehicle()
car.mileage=10
car.fuel_left=20
print(car.identify_distance_that_can_be_travelled())
        
