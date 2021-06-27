# exceptions helps us to respond to errors that are likely to occur.
# you place code that might cause an error in the try block. 
# code in the try block.
# code that should run in response to an error goes in the except block.

# code that should run only if the try block was successful goes in the else block.

prompt = "How many tickets do you need?"
num_tickets = input(prompt)

try:
    num_tickets = int(num_tickets)
except ValueError:
    print("please try again.")
else:
    print("your ticketls are printing.")