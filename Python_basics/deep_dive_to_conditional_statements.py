# conditional tests
car = 'bmw' # assignment operator
car == 'bmw' # relational operator

# ingnoring a case when making a comparision 

car = 'Audi'
car.lower() == 'audi' # True

# checking for inequality 
topping = 'mushrooms'
topping != 'anchovies' # True

# numerical comparison 
age = 18
age == 18 # true

age != 18 # false

# comparison operator 
age = 19
age < 21 # True
age <= 21 # True
age > 21 # False

age >= 21 #False

# checking for multiple conditions

age_0 = 22
age_1 = 18

# usning and to check 
age_0 >= 21 and age_1 >= 21  # False

age_1 = 23
age_0 >= 21 and age_1 >= 21 # True

# using or to check multiple conditions

age_0 = 22
age_1 = 18

age_0 >= 21 or age_1 >= 21 # True

age_0 = 18
age_0 >= 21 or age_1 >= 21 # False

# boolean values
# simple boolean values

game_active = True
can_edit = False

# if statements 
# simple if statements

age = 19
if age >= 18:
    print("You are eligible to vote!")

# if-else ladder statement

age = 12 
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your cose is $" + str(price) + ".")

# condition testing with list 

players = ['al', 'bey', 'cyn', 'date']

if 'al' in players:
    print(True)
if 'eric' in players:
    print(True)
else:
    print(False)


# conditional tests with lists(cont.)

banned_users = ['ann', 'chad', 'dee']
user = 'erin'

if user not in banned_users:
    print("You can play!")

# checking if a list is empty 
players = []
if players:
    for player in players:
        print("player: " + player.title())
else:
    print("We have no players yet!")

age = input("How old are you ? ")
age = int(age)

if age >= 18:
    print("\nYou can vote!")
else:
    print("\nSorry you can't vote!")


# while loops:
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1


# letting users choose when to quit

prompt = "\nTell me something, and I'll"
prompt += "repeat it back to you."
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# using a flag 
prompt = "\nTell me something, and I'll "
prompt += "repeat it back to you. "
prompt += "\n Enter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False

    else:
        print(message)

# breaking out of loops 
"""You can use the break statement and the continue,
statement with any of Python's loops.
For example you can use break to quit a for loop that's working through a list or a dictionary. 
You can use continue to skip over certain items when looping through a list or dictionary as well.
"""

# using continue in a loop
banned_users = ['eve', 'fred', 'gary', 'helen']

prompt = "\nAdd a player to your team."
prompt += "\n Enter 'quit' when you'are done."

players = []

while True:
    player = input(prompt)
    if player == 'quit':
        break
    elif player in banned_users:
        print(player + " is banned!")
        continue
    else:
        players.append(player)

print("\nYour team: ")
for player in players:
    print(player)


# avoiding infite loops

#while True:
 #   name = input("\nWho are you? ")
  #  print("Nice to meet you, " + name + "!")

# removing all instances of a value from a list

pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']
print(pets)

