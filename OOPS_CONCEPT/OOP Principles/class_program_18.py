# why do we need reference variables:
# बस इतना समझ लीजिए की अगर हीलीअम गैस से भरे गुब्बारे को किसी धागे से नहीं बाँधेंगे तो क्या होगा?
# गुब्बारा इधर-उधर उड़ जाएगा! 

class Mobile:
    def __init__(self, brand, price):
        print("Mobile created using location ID: ", id(self))
        self.brand = brand
        self.price = price
    
mob1 = Mobile("Apple", 25000)
print("Brand is ", mob1.brand, " and price is ", mob1.price)


mob2 = Mobile("Samsung", 15000)
print("Other brand is ", mob2.brand, " and its price is ", mob2.price)


# just like a baloon without a ribbon the an object without a reference variable cannot be used later

class Mobile2:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

Mobile2("Redmi", 9990)
# after the above line the mobile object is created is lost and unusable

# Multilple references 
# can a baloon have multiple ribbons? yes
# an object can have multiple references

# Notice the below code

class Mobile3:
    def __init__(self, brand, price):
        print("Inside constructor")
        self.brand = brand
        self.price = price
        print("Brand is: ", self.brand, " and price is ", self.price)

my_mob1 = Mobile3("Apple", 15000)
my_mob2 = my_mob1

print("ID for multiple reference of Same object, i.e my_mob1 ", id(my_mob1))
print("ID for multiple reference of Same object, i.e my_mob2 ", id(my_mob2))
