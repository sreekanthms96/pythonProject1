class BaseClass:
    def __init__(self):
        print("Base init")

    def set_name(self,name):
        self.name=name
        print("base class set_name")

class SubClass(BaseClass):

    def __init__(self):
        print("Subclass init")
    
    def set_name(self,name):
        self.name=name
        print("sub class set_name")

    def welcome(self):
        print("Welcome")

    def display_name(self):
        print("Name :" +self.name)


y = SubClass()
y.welcome()
y.set_name("Sreekanth MS")
y.display_name()