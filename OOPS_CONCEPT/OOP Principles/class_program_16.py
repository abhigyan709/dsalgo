# identifying invoking objects:

class Mobile:
    def __init__(self, price, brand):
        print("Mobile created with id: ", id(self))
        self.price = price
        self.brand = brand

    def return_product(self):
        print("Mobile being returned had ID ", id(self))
        print("Brand being retruned is ", self.brand, " and price is ", self.price)

mob1 = Mobile(12000, "Apple")
mob2 = Mobile(15000, "Samsung")
mob3 = Mobile(21999, "Redmi")

mob2.return_product() # invoking by feature 1
Mobile.return_product(mob3) # invoking by feature 2


