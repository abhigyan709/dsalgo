# updating the private data and its bad consequences

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
        print("The balance is ", self.__wallet_balance)
    
c1 = Customer(100, "Gopal", 24, 1000)
c1.__wallet_balance = 100000
c1.show_balance()

# as you can see there is no any change in the data so it is not producing the required results
