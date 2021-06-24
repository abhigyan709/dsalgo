# just like the ballons and ribbons, we can make one reference variable refer to another object.
# now any change made through this refernce varible will not affect the old object.

class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

mob1 = Mobile(1000, "Apple")
mob2 = mob1
mob2 = Mobile(2000, "Samsung")

print("Mobile", "Id", "Price")
print("mob1", id(mob1), mob1.price)
print("mob2", id(mob2), mob2.price)