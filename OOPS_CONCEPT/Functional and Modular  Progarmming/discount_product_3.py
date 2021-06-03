# upgraded version of previous version 
# previous version had a concern about some logic
# lets have some logic upon this 

def purchase_product(product_type,price,mobile_brand,material):
    if product_type == "Mobile":
        if mobile_brand == "Apple":
            discount = 10
        else:
            discount = 5
        total_price = price - price * discount / 100
    else:
        if material == "leather":
            tax = 5
        else:
            tax = 2
        total_price = price + price * tax / 100
    print("Total price of "+product_type+" is "+str(total_price))

purchase_product("Mobile",20000,"Apple",None)
purchase_product("Shoe",200,None,"leather")
                                                    