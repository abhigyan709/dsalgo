# Dictionaries in Python 
"""Python's dictionaries allow you to connect pieces of related information.
Each piece of information in a dictionary is stored as a key-value of pair.
You can loop through all the key-value pairs, all the keys, or all the values."""

alien_0 = {
    'color': 'green',
    'points': 5
}
print(alien_0)
# accessing the value with key
print(alien_0['color'])
print(alien_0['points'])

# adding new element with key as an index
alien_0['x'] = 0
alien_0['y'] = 25
alien_0['speed'] = 1.5

print(alien_0)

# adding element to dictionary is same as above

# dictionaries are mutable data types

alien_0['color'] = 'yellow'
alien_0['points'] = 9.0

print(alien_0)

# removing elements
del alien_0['points'] # deleting elements by its key
print(alien_0)


# looping through the key values
"""You can loop through a dictionary in 3 ways: 
1. through all the key-value pairs
2. all the keys
3. all the values
"""

fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in fav_languages.items():
    print(name + ": " + language) # looping through items

for name in fav_languages.keys():
    print(name) # looping through the keys

for language in fav_languages.values():
    print(language) # looping through values

for name in sorted(fav_languages.keys()):
    print(name + ": " + language) # sorted keys

num_responses = len(fav_languages)
print("Length of Dictionary: ", num_responses)

# nesting a list of dictionaries

users = []
new_user = {
    'last': 'fermi',
    'first': 'enrico',
    'username': 'enfermi',
}
users.append(new_user)
print(users)

new_user = {
    'last': 'curie',
    'first': 'marie',
    'username': 'mcurie',
}
users.append(new_user)
print(users)
