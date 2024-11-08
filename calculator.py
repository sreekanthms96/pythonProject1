from tkinter import *
window = Tk()

window.geometry("500x500")
window.title("Calculator")
window.config(bg="#8ee927")

def hello():
    print("button clicked")

button1=Button(text="OK",command=hello)
button2=Button(text="OK",command=hello)

button1.grid(row=0,column=0)
button2.grid(row=0,column=1)


window.mainloop()