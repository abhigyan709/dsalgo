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