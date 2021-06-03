# increasing the complexity
# now there will be two functions: purchase_mobile and purchase_shoes
# purchase_mobile() takes two parameters: price and brand
# purchase_shoe() takes two parameters: price and material
# if brand is apple discount is 10% else discount is 5%
# shoe material is "leather", tax is 5% else tax is 2%


def purchase_mobile(brand, price):
    if brand == "Apple":
        discount = 10
    else:
        discount = 5
    total_price = price - price * discount / 100
    print("Total price of " +brand+ " is " + str(total_price))

def purchase_shoe(material, price):
    if material == "leather":
        tax = 5
    else:
        tax = 2
    total_price = price + price * tax / 100
    print("Total price of " +material+ " is " + str(total_price))

purchase_mobile("Apple", 25000)
purchase_mobile("leather", 650)

