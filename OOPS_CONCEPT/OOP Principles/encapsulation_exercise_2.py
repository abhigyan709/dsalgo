class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, vehicle_cost, premium_amount):
        self.__vehicle_id = vehicle_id
        self.__vehicle_type = vehicle_type
        self.__vehicle_cost = vehicle_cost
        self.__premium_amount = premium_amount

    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def get_vehicle_id(self):
        return self.__vehicle_id

    def set_vehicle_type(self, vehicle_type):
        self.__vehicle_type = vehicle_type

    def get_vehicle_type(self):
        return self.__vehicle_type

    def set_vehicle_cost(self, vehicle_cost):
        self.__vehicle_cost = vehicle_cost

    def get_vehicle_cose(self):
        return self.__vehicle_cost

    def set_premium_amount(self, premium_amount):
        self.__premium_amount = premium_amount

    def get_premium_amount(self):
        return self.__premium_amount

    def calculate_premium():
        pass

    def vehicle_details():
        pass
