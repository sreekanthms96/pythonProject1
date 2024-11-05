#num = int(input("Enter a value: "))
def checkNegorPos(num):
    if num < 0:
        print("The number is Negative and value is " +str(num))
    elif num == 0:
        print("The number is zero")
    else:
        print("The number is positive and value is " +str(num))
