# accessing the private variables outside the class
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount

    def show_balance(self):
        print("The wallet balance is: ", self.__wallet_balance)

c1 = Customer(100, "Gopal", 24, 1000)
c1._Customer__wallet_balance = 1000000 # updates the value of the wallet_balance

c1.show_balance()

# but if the private variables can be accessed
# what is the advantage of making the variable private?
