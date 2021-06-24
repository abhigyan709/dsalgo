# we will implement the abstratcion here
# the purpose of using the method over object without knowing its internal classification is called abstration

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def purchase(self):
        print("Purchasing a mobile")
        print("Mobile: ", self.brand, "Price: ", self.price)

# print("Mobile 1")
mob1 = Mobile("Apple", 20000)
mob2 = Mobile("Samsung", 25666)
mob1.purchase()
mob2.purchase()

# here we are invoking the mobile object via purchase() method
# we are using this but we don't know the details and the working and this is called abstraction
