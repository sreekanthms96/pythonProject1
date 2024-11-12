from tkinter import *

# Initialize window
window = Tk()
window.geometry("400x500")
window.title("Simple Calculator")
window.config(bg="#8ee927")

# StringVar to store the current expression
expression = StringVar()

# Functions to handle button clicks and calculate the result
def press(num):
    current_exp = expression.get()
    expression.set(current_exp + str(num))

def clear():
    expression.set("")

def equal():
    try:
        # Evaluate the expression and display the result
        result = str(eval(expression.get()))
        expression.set(result)
    except Exception as e:
        expression.set("Error")

def backspace():
    current_exp = expression.get()
    # Remove the last character from the expression
    expression.set(current_exp[:-1])

# Display area
entry_field = Entry(window, textvariable=expression, font=('Arial', 20), bd=8, insertwidth=2, width=14, borderwidth=4)
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '.', '0', '⌫', '/',
    'C', '00', '%', '='
]

row_val = 1
col_val = 0

# Create buttons in a loop
for button in buttons:
    if button == "=":
        Button(window, text=button, width=10, height=3, bg="#d4a6f5", font=('Arial', 15),
               command=equal).grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)
    elif button == "C":
        Button(window, text=button, width=10, height=3, bg="#f5a6a6", font=('Arial', 15),
               command=clear).grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)
    elif button == "⌫":
        Button(window, text=button, width=10, height=3, bg="#f5d7a6", font=('Arial', 15),
               command=backspace).grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)
    else:
        Button(window, text=button, width=10, height=3, font=('Arial', 15),
               command=lambda btn=button: press(btn)).grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Make each column expand equally
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# Make each row expand equally
for i in range(1, 6):
    window.grid_rowconfigure(i, weight=1)

window.mainloop()
