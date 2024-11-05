value = 10 #global variable
def sample():
    print("The provided value is " +str(value))
sample()
print(value)

s=value+1 #this will add value from global variable
print(s)

#trying local and global variable with similar name

val = 35 #defining globally
def test():
    val=66
    print("The value is " +str(val))
test()  #this will actually take values from local variable
print(val) #this will print from global