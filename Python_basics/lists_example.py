# list 
# list stores a series of items in a particular order.
# you access the items using an index, or within a loop.

# make a list
names = ["abhigyan", "pushkar", "hritik"]

# get the first item in the list
first_person = names[0]
print(first_person)

# get the last item in the list
last_person = names[-1]
print(last_person)

# looping through the list
for name in names:
    print(name, len(name))

# adding items to the list 
bikes = []
bikes.append('trek')
bikes.append('readline')
bikes.append('giant')
print(bikes)

# making numerical lists
squares = []
for x in range(1, 11):
    squares.append(x ** 2)
print("List of squares from 1 to 10: ", squares)

# List comprehensions
cube_root = [x**3 for x in range(1, 11)]
print("List of cube from 1 to 10: ", cube_root)


# list comprehension using lambda function 
cubes = list(map(lambda x: x**3, range(1, 11)))
print("Cubes using lambda function: ", cubes)

# slicing a list 
finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]
print(first_two)

# copying a list
copy_of_bikes = bikes[:]
print(copy_of_bikes)

