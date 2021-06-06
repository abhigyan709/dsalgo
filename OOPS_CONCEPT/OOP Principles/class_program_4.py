# assigning and adding additional attributes to the specific objects

class Mobile:
    pass

mob1 = Mobile()
mob2 = Mobile()

mob1.brand = "Apple"
mob2.brand = "Samsung"

mob1.ios_version = 10

mob1.price = 20000
mob2.price = 3000

print(mob1.brand, mob1.ios_version, mob1.price)
print(mob2.brand, mob2.price)
