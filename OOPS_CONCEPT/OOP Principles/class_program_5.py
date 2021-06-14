# in python if we assign a value to a non exixtant attribute,
# it will create that attribute for that object alone.
# this program will show the result of assigning v/s updating 

class Mobile:
    pass

mob1 = Mobile()
mob2 = Mobile()

mob1.price = 20000
mob1.brand = "Apple"
mob1.ios_version = 10

mob1.ios_version = 11

mob2.price = 3000
mob2.brand = "Samsung"

mob2.android_version = "Marshmallow"

print(mob1.ios_version)
print(mob2.android_version)