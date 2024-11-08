class BaseClass:
    def __init__(self):
        print("BaseClass init")

    def set_name(self,name):
        self.name=name
        print("base class set_name")

class SubClass(BaseClass):

    def __init__(self):
        super().__init__() #standard method for calling Baseclass constructor
        BaseClass.__init__(self) #this will also call Baseclass constructor
        print("Subclass init")
    
    def set_name(self,name):
        self.name=name
        super().set_name(name) #to call base class set_name() to prevent overriding
        print("sub class set_name")

    def welcome(self):
        print("Welcome")

    def display_name(self):
        print("Name :" +self.name)


y = SubClass()
y.welcome()
y.set_name("Sreekanth MS")
y.display_name()