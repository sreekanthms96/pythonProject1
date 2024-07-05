# a = input("Enter a number")
# b = input("Enter a number")
# print("Hi, Hello" + (a) + " second value is " + (b))
# sum = int(a) + int(b)
# print("Result is " + str(sum))



# immutable values are non-changeable of string in python
# mutable values of string in python as shown below

list=["sree","sree2","sree3"]
list[1]="test"

# to add values to a specific list we can use the following commands

list=list + ["sreekanth", 18]

list.append("hai") #append commands use to append a value into that string
list.append(input("enter a value: "))  # this is to input a user defined value to the list
print(list)
print(list[0])    #to print values at array0 position