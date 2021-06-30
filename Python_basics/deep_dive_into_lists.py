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

for numbers in range(1001): # syntax of range: range(start, stop, step)
    print("Number: ", numbers)

# basic statstics in list:
ages = [25, 26, 28, 19, 18, 17, 35, 36]
sum_ages = sum(ages)
min_ages = min(ages)
max_ages = max(ages)

print("Sum of ages: ", sum_ages)
print("Youngest: ", min_ages)
print("Oldest: ", max_ages)


# slicing a list 
"""You can work with any set of elements from a list.
A portion of a list is called a slice.
"""
# getting the 1st 3 elements:
finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
print("Finishers: ", finishers)
first_3 = finishers[:3]
print("Fisrt 3 finishers: ", first_3)

middle_3 = finishers[1:4]
print("Middile 3 finishers: ", middle_3)

last_3 = finishers[-3:]
print("Last 3 of finishers: ", last_3)

# copy of a list
copy_of_list = finishers[:]
print(copy_of_list)

# list comprehension
"""To use a list comprehension, define an expression for the values you want to store in the list.
Then write a for loop to generate input values needed to makes the list."""

square = []
for x in range(10):
    square.append(x**2)
print(square)
squares = list(map(lambda x: x**2, range(10))) # list comprehension
print(squares)

"""another method
list comprehension"""

cubes = [x**3 for x in range(10)]
print(cubes)

"""a list comprehension consists of brackets containing an expression followed by a for clause, 
then zero or more for or if clauses.
The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
For example: """

my_tuple = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(my_tuple)

my_tuple_2 = [(x, y) for x in [1, 2, 3] for y in [2, 2, 2] if x == y]
print(my_tuple_2)

"""nested list comprehension can be any arbitrary expression, including another list comprehenshion.
Consider the following example of 3 * 4 matrix implemented as a list of 3, 
length of 4: """

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

new_mat = [[row[i] for row in matrix] for i in range(4)]
print(new_mat)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)


"""using a loop to convert a list of names to upper case"""
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = []
for name in names:
    upper_names.append(name.upper())
print(upper_names)

"""Another Methods"""
names_2 = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names_2 = [nam.upper() for nam in names_2]
print(upper_names_2)


# tuples in the python 
"""A tuple is like a list but it is immutable in nature.
We can overwrite an entire tuple but you can't change the individual elements in a tuple.
"""

"""Defining a tuple"""

dimensions = (800, 600)

for dimension in dimensions:
    print(dimension)

dimensions = (800, 1080) # tuple over written


