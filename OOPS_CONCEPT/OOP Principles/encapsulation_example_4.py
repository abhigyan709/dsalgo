# how does the code encapsulation work
# generally python will interanlly change its name to _Classname__attribute.

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
print(c1.__wallet_balance)