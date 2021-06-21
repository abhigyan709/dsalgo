# objects and class:
class Mobile:
    pass
mob1 = Mobile() # object 1
mob2 = Mobile() # object 2
mob3 = Mobile() # object 3

# every object is unique, even it is looking same
# just like twins, the may have same face, 
# but they will be having unique finger print

print("ID of Object 1: ", id(mob1))
print("ID of Object 2: ", id(mob2))
print("ID of Object 3: ", id(mob3))

# Creating attributes & Assigning values to them 
mob1.brand = "Apple"
mob2.brand = "Samsung"
mob3.brand = "Redmi"

mob1.price = 25000
mob2.price = 15000
mob3.price = 7500

print("Objetc 1, Brand 1: ", mob1.brand, "Price: ", mob1.price)
print("Objetc 2, Brand 2: ", mob2.brand, "Price: ", mob2.price)
print("Objetc 3, Brand 3: ", mob3.brand, "Price: ", mob3.price)

# adding more attributes to the object 
mob1.ios_version = 11
mob2.samsung_UI = 2.5
mob3.MI_UI = 12.0

print("iOS Version of Apple: ", mob1.ios_version)
print("Samsung UI version of Samsung: ", mob2.samsung_UI)
print("MIUI Version of Redmi: ", mob3.MI_UI)