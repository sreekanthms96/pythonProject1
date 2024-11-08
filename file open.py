with open("D:\Python\pythonProject1\date_time.py", "r") as f:
    x = f.read()
print(x) #to read the file


#f.open("filepath", "wb+)  #to write into a file
# f.write("print('HI')") 
# f.close()


with open("D:\Python\pythonProject1\sreekanth.py", "wb+") as f:
    x = f.write("print('Hello')".encode())
print(x) #this is also used to write into the file
 