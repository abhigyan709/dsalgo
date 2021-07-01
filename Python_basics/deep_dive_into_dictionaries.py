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

for user_dict in users:
    for k, v in user_dict.items():
        print(k + ": " + v)
    print("\n")

# define a list of users, where each user is represented by a dictionary 
users_2 = [
    {
        'last': 'kumar',
        'first': 'abhigyan',
        'username': 'akumar',
    },
    {
        'last': 'kumar',
        'first': 'gyanu',
        'username': 'gkumar',
    }
]

for user_dic in users_2:
    for u, p in user_dic.items():
        print(u + ": " + p)
    print("\n")

# list in a dictionary
# storing multiple languages for each person.
fav_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, langs in fav_languages.items():
    print(name + ": ")
    for lang in langs:
        print("- " + lang)

# Dictionary of Dictionaries
my_user = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last' : 'curie',
        'location' : 'paris',
    },
}

for username, user_dictionary in my_user.items():
    print("\nUsername: " + username)
    full_name = user_dictionary['first'] + " "
    full_name += user_dictionary['last']
    location = user_dictionary['location']

    print("\tFull Name: " + full_name.title())
    print("\tLocation: " + location.title())


# levels of Nesting: 
# using an OrderedDict:
"""Standard python dictionaries don't keep track of the order in which keys and values are added;
they only preserve the association between  each key and its value.
If you want to preserve the order in which keys and values are added, use an OrderedDict.
"""


from collections import OrderedDict
fav_languages = OrderedDict()

fav_languages['jen'] = ['python', 'ruby']
fav_languages['sarah'] = ['c', 'c++']
fav_languages['edward'] = ['ruby', 'go']
fav_languages['phil'] = ['python', 'haskel']

# display the result in same order they 
# were entered

for name, langs in fav_languages.items():
    print(name + ": ")
    for lang in langs:
        print("- " + lang)

# making a million dictionaries
aliens = []
for alien_num in range(1000000):
    new_alien = {}
    new_alien['color'] = 'green'
    new_alien['points'] = 5
    new_alien['x'] = 20 * alien_num
    new_alien['y'] = 0
    aliens.append(new_alien)

num_aliens = len(aliens)

print("Number of aliens created: ")
print(num_aliens)
print(aliens)