# list is a type of an array/or simply array 
# its same like any other languages having arrays

# it stores a series of items in a particular order.
# allows to store sets of information in one place,
# whether you have just a few items or millions of items.

# one of the most poweful feature in Python

# Defining a list
# Making a List
users = ['val', 'bob', 'mia', 'ron', 'ned']

# accessing the elements
# indexing starts from 0 from L -> r

first_user = users[0] # first element

second_user = users[0] # second user

newest_user = users[-1] # last element

# modifying individual items

users[0] = 'valerie'
users[-2] = 'ronald'

# printing the list:
print("Here is my List: ",users)

# adding elements, appending

users.append('amy') # adding an element to end of list

new_users = []
new_users.append('val')
new_users.append('bob')
new_users.append('mia')

# inserting elements at particular position
new_users.insert(0, 'joe')
new_users.insert(3, 'bea')

print("My new list: ", new_users)

del users[2]
print("Deleted list: ", users)

# removing an item by its value
print(new_users.remove('mia'))
print("After remove: ", new_users)

# popping elements
"""If you want to work with an element that you are removing 
from the list, you can 'pop' the element.
If you thing of the list as a stack of items, pop() takes an items, 
pop() takes an item off the top of the stack.
By default pop() returns the last element in the list, 
but you can also pop elements from any position in the list"""

# pop the last element from a list 
most_recent_user = users.pop()
print(most_recent_user)

# pop the last item from a list
first_user = users.pop(0)
print(first_user)

# length of the list 
num_users = len(new_users)
print("There are " + str(num_users) + " users in new_list.")

# list sorting
"""The sort() method changes the order of a list permanently.
The sorted() function returns a copy of the list, leaving the original list unchanged.
You can sort the items in a list in alphabetical order or reversed alpabetical order.
"""

# list sorting permanently
users.sort()

users.sort(reverse=True)

# sorting a list temporarily
print(sorted(users))
print(sorted(users, reverse = True))

# reversing the order of a list
users.reverse()
print(users)

# looping through the lists
"""Lists can have millions of items, so python provides an efficient way to loop through all the items in a list.
When you set up a loop, Python pulls each item from the list one at a time
and stores it in a temporary variable, which you provide a name for. 
This name should be a singular version of the list name.
The indented block of code makes up the body of the loop, where you can work with each individual item.
Any lines that are not indented run after the loop is completed."""

# print all items and len in the list

for user in users:
    print(user, len(user))

# printing a message for each item, and a seperate message afterwards

for user in users:
    print("Welcome, " + user + "!")
print("Welcome you all!")


# The range() function
"""You can use the range() function to work with a set of numbers efficiently.
The range() functions starts at by default, and stops one number below the number passed to it.
You can use the list() function to efficiently generate a large list of numbers.
 """

# printing the numbers fron 0 to 1000

for numbers in range(1001):
    print("Number: ", numbers)

print(numbers)