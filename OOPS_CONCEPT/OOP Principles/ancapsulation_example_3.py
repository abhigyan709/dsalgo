# restricting the access of vulnarable code

class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance # data encapsulated

    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount
        
    def show_balance(self):
        print("The balance is ", self.__wallet_balance)

c1 = Customer(100, "Gopal", 24, 1000)
print(c1.__wallet_balance)

c2 = Customer(101, "Shyam", 25, 2000)
print(c2.__wallet_balance)

# this is the difference of data encapsulation & open data
# accessing this data resulting in Runtime Exception 
