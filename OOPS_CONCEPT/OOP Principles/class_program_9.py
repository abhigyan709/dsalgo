# Class program showing example of constructor
# self is not a keyword. self refers to the current object being executed.
class Mobile:
    def __init__(self) -> None:
        print("Id of self in constructor: ", id(self))

mob1 = Mobile()