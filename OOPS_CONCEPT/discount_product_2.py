def purchase_product(product_type, price, mobile_brand = None):
    if product_type == 'Mobile':
        if mobile_brand == 'Apple':
            discount = 10
        else:
            discount = 5
        total_price = price - price * discount / 100
    else:
        total_price = price + price * 2 /100
    print("Total price of: " +product_type+ " is "+str(total_price))

purchase_product("Mobile", 20000, "Apple")
purchase_product("Shoe", 200)

# logic
# if product type will be mobile & brand is apple: then discount is 10%
# else for the other brand discount will be 5%

# now if the product will be other than mobile extra 2% of the tax will be added