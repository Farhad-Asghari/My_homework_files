#38. Create a class CalculatorApp that uses tkinter to create a simple calculator GUI.

import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        self.result_var = tk.StringVar()

        self.entry = tk.Entry(master, textvariable=self.result_var, width=16, font=('Arial', 24), bd=10, insertwidth=2)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(master, text=button, padx=20, pady=20, command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        elif char == 'C':
            self.result_var.set("")
        else:
            current = self.result_var.get()
            self.result_var.set(current + char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
