class Mobile:
    def __init__(self, brand, price):
        print("Inside Constructor")
        self.brand = brand
        self.price = price

    def purchase(self):
        print("Purchasing a mobile")
        print("The mobile has brand", self.brand, "and price", self.price)

print("Mobile-1")
mob1 = Mobile("Apple", 20000)
mob1.purchase()

print("Mobile-2")
mob2 = Mobile("Samsung", 8000)
mob2.purchase()

