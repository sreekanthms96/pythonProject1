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

print(Third.mro()) #defines the order in which classes are accessed when searching for a method or attribute in the context of inheritance (method resolution order). example shown below:

#[<class '__main__.Third'>, <class '__main__.Second'>, <class '__main__.First'>, <class 'object'>]

