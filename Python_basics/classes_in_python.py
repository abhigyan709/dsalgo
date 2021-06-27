# a class defines the behaviour of an object and the kind of information an object can store.
# the information in a class is stored in attributes,
# and function that belong to a class are called methods. 
# A child class inherits the attributes and methods from its parent class.

class Dog:
    def __init__(self, name):
        self.name = name

    def sit(self):
        print(self.name + " is sitting.")

my_dog = Dog('Peso')
# my_dog.name = 'Peso'

print(my_dog.name + " is a grat dog!")
my_dog.sit()


# inheritance in class

class SARDog(Dog):
    """This class will inherit the property 
    of the above Dog class."""

    def __init__(self, name):
        super().__init__(name)
    
    def search(self):
        """Simulate searching."""
        print(self.name + " is searching!")

my_dog = SARDog('Williw')
print(my_dog.name + " is a search dog.")
my_dog.sit()