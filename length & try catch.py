# a="Hi, you are doing this codes to print the total no of length of this text assigned in a"
# print(len(a))

# #to find the word in the 52nd position of this array

# print(a[52])

# #array is starting from position 0



# #to print word from 49 to 79 we use 49:79 commands

# print(a[49:79])

b=int(input("Enter a number: "))

try:
    a=10/b
    print(a)
    print("Try completed and value is "+str(a))
except ZeroDivisionError:
    print("OH... sorry Cant Divide with zero")
print("program completed")