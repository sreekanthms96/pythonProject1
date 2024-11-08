import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x500")

        self.expression = ""
        self.display_text = tk.StringVar()

        # Display Frame
        display_frame = tk.Frame(self.root)
        display_frame.pack(expand=True, fill="both")

        display_entry = tk.Entry(display_frame, textvariable=self.display_text, font=("Arial", 20), borderwidth=5, justify="right")
        display_entry.pack(expand=True, fill="both")

        # Buttons Frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(expand=True, fill="both")

        # Button Layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ]
        # Create and place buttons on the grid
        for (text, row, col) in buttons:
            button = tk.Button(buttons_frame, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Clear button
        clear_button = tk.Button(buttons_frame, text="C", font=("Arial", 18), command=self.clear_expression)
        clear_button.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Adjust grid weights for resizing
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
            buttons_frame.columnconfigure(i % 4, weight=1)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.display_text.set(result)
                self.expression = result
            except:
                self.display_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.display_text.set(self.expression)

    def clear_expression(self):
        self.expression = ""
        self.display_text.set("")

# Run the calculator
root = tk.Tk()
calc = Calculator(root)
root.mainloop()
