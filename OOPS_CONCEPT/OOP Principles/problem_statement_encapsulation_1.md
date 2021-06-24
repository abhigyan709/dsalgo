# Consider the following code and case and solve as directed

In the Athlete class given below, 

make all the attributes private and
add the necessary accessor and mutator methods
Represent Maria, the runner and make her run.

    #lex_auth_01275045546160947226
    class Athlete:
        def __init__(self,name,gender):
            self.name=name
            self.gender=gender

        def running(self):
            if(self.gender=="girl"):
                print("150mtr running")
            else:
                print("200mtr running")
                                        