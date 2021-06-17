# Class program showing example of constructor
# self is not a keyword. self refers to the current object being executed.
class Mobile:
    def __init__(self) -> None:
        print("Id of self in constructor: ", id(self))

mob1 = Mobile()

# we can create a constructor without parameters. But this is rarely useful, see the below code.
print("we can create a constructor without parameters. But this is rarely useful, see the below code.")

class Mobile2:
    def __init__(self) -> None:
        print("Inside Constructor")

mob1 = Mobile2()
mob2 = Mobile2()