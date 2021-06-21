# if statements 
# if statements are used to test for particular conditions and respond appropriately.

# Conditional test
"""
equals: x == 42
not equals: x != 42
greater than: x > 42
greater than or equal to:  x >= 42
less than: x < 42
less than or equal to: x <= 42
"""

# conditional checks in the list
bikes = ['trek', 'mob', 'spoof', 'delta']
'trek' in bikes # here the in keyword checks for the condition

'surely' not in bikes


# a simple if test:
age = int(input("Please enter your age: "))
if age >= 18:
    print("You can vote.")


# if else ladded statements: 

if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
else:
    ticket_price = 15
print("Ticket price: ", ticket_price)