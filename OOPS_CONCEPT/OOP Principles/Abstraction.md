# Abstraction in Python 
## OOPs principle 

### Consider the following code

    class Mobile:
        def __init__(self, brand, price):
            print("Inside Constructor")
            self.brand = brand
            self.price = price

        def purchase(self):
            print("Purchasing a Mobile")
            print("This mobile has brand", self.brand, "and price", self.price)

    print("Mobile-1")
    mob1 = Mobile("Apple", 20000)
    mob1.purchase()

    print("Mobile-2")
    mob2 = Mobile("Samsung", 3000)
    mob.purchase()

### So what is abstraction?
The ability to use something without having to know the details of how it is working is called **Abstraction**

in the above code we are invoking the method purchase() on mobile object, but we dont have to know the details of the method to invoke it.

