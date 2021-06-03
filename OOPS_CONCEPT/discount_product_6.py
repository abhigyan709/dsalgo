# version 6 upgraded to the global varibles

total_price_mobile = 0
total_price_shoe = 0

def purchase_mobile(price, brand):
    global total_price_mobile
    if brand == "Apple":
        discount = 10
    else:
        discount = 5
    total_price_mobile = price - price * discount / 100
    print("Total price for mobile is "+str(total_price_mobile))

def purchase_shoe(price, material):
    global total_price_shoe
    if material == "leather":
        tax = 5
    else:
        tax = 2
    total_price_shoe = price + price * tax / 100
    print("Total price for shoe is: "+str(total_price_shoe))

def return_mobile():
    print("Refund price for mobile is: ", total_price_mobile)

def return_shoe():
    print("Refund price of shoe is: "+total_price_mobile)


purchase_mobile(20000, "Apple")
purchase_shoe(200, "leather")
return_mobile()