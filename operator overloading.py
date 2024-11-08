#operator overloading

class sample:
    def set_name(self,name):
        self.name=name
    
    def __add__(self,other):
        name=self.name+" "+other.name
        return name

first_name = sample()
second_name = sample()

first_name.set_name("Sreekanth")
second_name.set_name("MS")
full_name=first_name+second_name

print(full_name)

#Explanation

   # __add__ Method: This is a special method in Python that allows you to define how the + operator should behave when applied to instances of your class. By defining __add__, you allow + to be used between two sample objects.

    #Code Walkthrough:
       # The sample class has a set_name method to set the name attribute.
       # The __add__ method takes two objects (self and other), accesses their name attributes, and concatenates them. This returns the combined name.


