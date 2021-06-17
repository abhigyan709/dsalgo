# attributes can be added to a class through a special function calles __init__().

# lets see how we can create mobile class:

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
mob1 = Mobile("Apple", 20000)
mob2 = Mobile("Samsung", 8000)

print(mob1.brand, mob1.price)
print(mob2.brand, mob2.price)