# the below code allows us to purchase different product at discount rate
# the discount rate is set to: 10
def purchase_product(product_type, price):
    discount = 10
    total_price = price - price * discount / 100
    print("Total price of " +product_type+ " is "+str(total_price))

purchase_product("Mobile", 20000)
purchase_product("Shoe", 200)
