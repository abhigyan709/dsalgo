# list of objects

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

mob1 = Mobile("Apple", 1000)
mob2 = Mobile("Samsung", 2000)
mob3 = Mobile("Apple", 3000)
mob4 = Mobile("Samsung", 4000)
mob5 = Mobile("Apple", 5000)

list_of_mobile = [mob1, mob2, mob3, mob4, mob5]

for mobile in list_of_mobile:
    print(mobile.brand, mobile.price)