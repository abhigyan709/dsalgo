# while loop repeats a block of code as long as a particular condition remains true

# a simple value
current_value = 1
while current_value <= 5:
    print(current_value)
    current_value += 1

# letting the user to choose when to quit
msg = ''
while msg != 'quit':
    msg = input("What's your message? ")
    print(msg)
