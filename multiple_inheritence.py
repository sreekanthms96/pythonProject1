#Multilevel inherittence

class First:
    def diplay_First(self):
        print("First")
class Second(First):
    def display_Second(self):
        print("Second")

class Third(Second):
    def display_Third(self):
        print("Third")

x = Third()
x.diplay_First()
x.display_Second()
x.display_Third()



#multiple inheritence

class First:
    def diplay_First(self):
        print("First")
class Second():
    def display_Second(self):
        print("Second")

class Third(First,Second):
    def display_Third(self):
        print("Third")

x = Third()
x.diplay_First()
x.display_Second()
x.display_Third()


