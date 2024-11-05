value = 10
def sample():
    print("The provided value is " +str(value))
sample()
print(value)



#trying local and global variable with similar name

val = 35 #defining globally
def test():
    val=66
    print("The value is " +str(val))
test()  #this will actually take values from local variable
print(val) #this will print from global