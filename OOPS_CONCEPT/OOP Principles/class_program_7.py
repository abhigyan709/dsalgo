# best practices to assign the attributes

class Mobile:
    pass

mob1 = Mobile()
mob2 = Mobile()

mob1.price = 20000
mob1.brand = "Apple"
mob1.ios_version = 11
print(mob1.ios_version)

mob2.price = 3000
mob2.brand = "Apple"
mob2.ios_versio = 11 # typo error pay attention to this 
print(mob2.ios_versio) # still working because python allows to create new attribute on spot
