# attribute error
# accessing non-existing attributes

class Mobile:
    pass

mob1 = Mobile()
mob2 = Mobile()

mob1.price = 20000
mob1.brand = "Apple"
mob1.ios_version = 10

mob2.price = 3000
mob2.brand = "Samsung"
mob2.android_version = "Marshmallow"

print(mob1.ios_version)
print(mob2.ios_version)