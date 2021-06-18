# attribute creation using self....

class Mobile:
    def __init__(self, price, brand):
        print("Id of self in constructor", id(self))
        self.price = price
        self.brand = brand

mob1 = Mobile(1000, "Apple")
print("Id of mob1 in driver code", id(mob1))

mob2 = Mobile(1000, "Apple")
print("Id of mob2 in driver code", id(mob2))


class Mobile2:
    def __init__(self):
        print("Inside the mobile constructor")
        self.brand = None
        brand = "Apple" # local variable, variable without self.
        """
        This is local variable.
        Variables without self are local and they don't
        affect the attributes.
        """

        # local variable cannot be accessed outside the init
        # using self creates attributes which are
        # accessible in other methods as well

mob_1 = Mobile2()
print(mob_1.brand) 
# this does not print apple
# this prints None because brand = Apple creates
# a local variable and it does not affect the attribute.