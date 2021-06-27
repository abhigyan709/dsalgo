# function is a block of code designed in any languge to do/perform a certain task
# information passed to a function in a certain code is called an argument
# information recieved by a function is called a parameter 

# a simple function 

def greet_user():
    """Display a simple greeting"""
    print('Hello User!')

greet_user()


# passing an argument
def greet_user(username):
    """Display a personalised greeting."""
    print("Hello, " + username + "!")

greet_user('abhigyan709')


# dafault values for parameters
def make_pizza(topping='bacon'):
    """Make a single - topping pizza."""
    print("Have a " + topping + " pizza!")

make_pizza()
make_pizza('pepperoni')

# returning a value of function 
def add_numbers(x, y):
    """Add two numbers and return the sum."""
    return x + y

sum = add_numbers(3, 5)
print(sum)
