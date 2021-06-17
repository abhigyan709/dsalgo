# attributes can be added to a class through a special function calles __init__().

# lets see how we can create mobile class:

class Mobile:
    def __init__(self, brand, price): # brand and price are parameters
        self.brand = brand # attributes
        self.price = price # attributes
mob1 = Mobile("Apple", 20000)
mob2 = Mobile("Samsung", 8000)

print(mob1.brand, mob1.price)
print(mob2.brand, mob2.price)

# Note: The parameters names and attribute names need not match.