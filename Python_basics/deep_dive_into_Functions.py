# what are functions?

"""Functions are named blocks of code
designed to do one specific job.
Functions allow you to write code
once that can then, be run whenever you need
to accomplish the same task. Functions can take 
in the information they need, and return the information they generate.
Using functions effectively makes your programs
easier to write, read, test & fix.
"""

# Defining a function
"""The first line of the program for function is its definition, 
marked by the keyword def.

The name of the function is followed by a set 
of parantheses and a colon. 
A docstring, in triple quotes, describes what the function does.
The body of a function is indented one level.

To call a function, give the name of the function followed by a set of parantheses.

"""

# make a function

def greet_user():
    """Display a simple greeting."""
    print("Hello")

greet_user()

# Passing information to a function.

"""information that's passed to a function is called an 
argument; information that's received by a function is called 
a parameter. Arguments are included in parentheses after 
the function's name, and parameters are listed in 
parentheses in the function's definition"""

def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username + "!")

greet_user('jessie')
greet_user('diana')
greet_user('brandon')
