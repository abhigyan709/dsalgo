# one object multiple reference example
"""
The below program shows that if there is changes in reference
variable, it gets also reflected in another variable too!
because there is only one object and we are creating multiple 
reference variable for same object.
"""
class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
    
mob1 = Mobile(10000, "Apple")
print("Price of mobile 1: ", mob1.price)

mob2 = mob1
mob2.price = 3000

print("Price of mobile 1: ", mob1.price)
print("Price of mobile 2: ", mob2.price)