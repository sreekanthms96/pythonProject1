class First:
    def display(self):
        print("First")
class Second():
    def display1(self):
        print("Second")

class Third(First,Second):
    def display_Third(self):
        print("Third")

x = Third()

x.display()
x.display_Third()