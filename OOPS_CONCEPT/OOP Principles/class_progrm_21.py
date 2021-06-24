# Prinitig an object

class Shoe:
    def __init__(self, price, material):
        self.price = price
        self.material = material

s1 = Shoe(1000, "Canvas")
print(s1)

# the above print of s1 object is not in more readable format, it gives hexagonal form
# to implement the more readable format for prining the object we will use __str__ method

# let's get started to see how it works

class Shoe2:
    def __init__(self, price, material):
        self.price = price
        self.material = material

    def __str__(self):
        return "Shoe with price " + str(self.price) + " and material: " + self.material

s1 = Shoe2(2000, "leather")
print(s1)