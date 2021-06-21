# dictionaries
# they are the mutable data types
# dictionaries stores connections between pieces of information
# each item in a dictionary is a key-value pair.

# a simple dictionary
alien = {
    'color': 'green',
    'points': 5
}

# accessing a value 
print("The alien's color is ", alien['color'])

# adding a new key-value pair
alien['x_position'] = 0

# looping through all key-value pairs
fav_numbers = {
    'eric': 17,
    'ever': 14,
}
for name in fav_numbers.keys():
    print(name + ' loves a number')