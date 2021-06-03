# buying 2 mobile 
# returning only one 1 phone
# making sure that purchase_shoe() function won't accidentally modify the global value for mobile
# complication is increasing now

total_price_mobile = 0
total_price_shoe = 0

def purchase_mobile(price, brand):
    global total_price_mobile
    if brand == "Apple":
        discount = 10
    else:
        discount = 5
    total_price_mobile = price - price * discount / 100
    print("Total price for Mobile is "+str(total_price_mobile))

def purchase_shoe(price, material):
    global total_price_shoe
    if material == "leather":
        tax = 5
    else:
        tax = 2
    total_price_shoe = price + price * tax / 100
    print("Total price for shoe is "+str(total_price_shoe))

def return_mobile():
    print("Refund price of the shoe is: ", total_price_mobile)

def return_shoe():
    print("Refund price for shoe is ", total_price_shoe)

purchase_mobile(20000, "Apple")
purchase_shoe(200, "leather")
purchase_mobile(2000, "Samsung")
return_mobile()

