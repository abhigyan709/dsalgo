# parameterless and parameterized constructor

class Mobile:
    def __init__(self, one, two):
        print("Inside Constructor")
# uncomment the beclow code and see the error

# mob1 = Mobile() # throws error because required arguments 
# mob2 = Mobile(100, 20, 30) # this will also throw an error by giving required 2 but 3 given