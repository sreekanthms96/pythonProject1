class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    
    def display(self):
        print("The Make is :"+self.make)
        print("The Model is :"+str(self.model))
        print("The manufacturing year is :"+str(self.year))

x = car("BMW","M5",2017)
y = car("Benz", "S-Class", 2018)

x.display()
y.display()