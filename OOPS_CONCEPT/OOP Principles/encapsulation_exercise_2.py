def check_type(type):
    vehicle_type = ["Two Wheeler", "Four Wheeler"]
    if type not in vehicle_type:
        return 0
    return 1

class Vehicle:
    def __init__(self):
        self.__vehicle_id = None
        self.__vehicle_type = None
        self.__vehicle_cost = None
        self.__premium_amount = None

    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def set_vehicle_type(self, vehicle_type):
        if check_type(vehicle_type):
            self.__vehicle_type = vehicle_type
        else:
            return "Invalid Vehicle Details"

    def set_vehicle_cost(self, vehicle_cost):
        self.__vehicle_cost = vehicle_cost
    def set_premium_amount(self, premium_amount):
        self.__premium_amount = premium_amount

    def get_vehicle_id(self):
        return self.__vehicle_id
    def get_vehicle_type(self):
        return self.__vehicle_type
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    def get_premium_amount(self):
        return self.__premium_amount

    def calculate_premium(self):
        if self.__vehicle_type == "Two Wheeler":
            self.__premium_amount = self.__vehicle_cost * 2/100
        elif self.__vehicle_type == "Four Wheeler":
            self.__premium_amount = self.__vehicle_cost * 6/100
        else:
            print("Please enter correct vehicle type")

    def display_vehicle_details(self):
        print("Vehicle ID: ", self.__vehicle_id)
        print("Vehicle Type: ", self.__vehicle_type)
        print("Vehicle Cost: ", self.__vehicle_cost)
        print("Premium: ", self.__premium_amount)

bike = Vehicle()
bike.set_vehicle_id(5695)
bike.set_vehicle_type("Two Wheeler")
bike.set_vehicle_cost(59000)
bike.calculate_premium()
bike.display_vehicle_details()

        