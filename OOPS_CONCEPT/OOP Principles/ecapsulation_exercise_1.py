#lex_auth_01275045546160947226
class Athlete:
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender

    def running(self):
        if(self.__gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_gender(self, gender):
        self.__gender =gender

    def get_gender(self):
        return self.__gender

Maria = Athlete("Maria", "girl")
Maria.running()



                                        