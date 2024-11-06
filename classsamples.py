class MySampleClass:
    year=2024

    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

    def add_age(self):
        self.age=self.age+1

    def relocate(self,place):
        self.place=place
    
    def display(self):
        print("Year : "+str(MySampleClass.year))
        print("Name : "+self.name)
        print("Age : "+str(self.age))
        print("Place : "+self.place)
    
    @classmethod
    def add_year(cls):
        MySampleClass.year=MySampleClass.year+1

    @staticmethod
    def display_welcome():
        print("Welcome")

x = MySampleClass("Sreekanth",28,"Kochi")
y = MySampleClass("Test User",23,"Kochi")

x.display()
y.display()

print("-------------------------")

MySampleClass.year=MySampleClass.year+1

x.add_age()
y.add_age()
x.relocate("Delhi")
y.relocate("Mumbai")

x.display()
y.display()

print("-------------------------")

MySampleClass.add_year()
MySampleClass.display_welcome()