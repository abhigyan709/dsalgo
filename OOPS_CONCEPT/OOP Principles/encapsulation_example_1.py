# data encapsulation 

class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.wallet_balance = wallet_balance

    def __str__(self):
        return "Customer ID: " + str(self.cust_id)

    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance += amount
    
    def show_balance(self):
        print("The balance is ", self.wallet_balance)

c1 = Customer(100, "Gopal", 24, 1000)
c1.update_balance(500)
# print(c1.cust_id)
c1.show_balance()

