# what happens when we pass an object as a parameter to a functionn?
# In the below code, what will be the output?

class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

def change_price(mobile_obj):
    mobile_obj.price = 3000

mob1 = Mobile(1000, "Apple")
change_price(mob1)
print(mob1.price)

class Mobile2:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def change_price(mobile_obj):
        print("ID of the object inside the function: ", id(mobile_obj))
        mobile_obj.price = 3000

mob2 = Mobile2(1000, "Apple")
print("ID of object in driver code: ", id(mob2))
mob2.change_price()
print("price of mob2: ", mob2.price)


# the above example shows that 