#39. Create a class LoginApp  uses tkinter to create a  GUI .

import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, master):
        self.master = master
        master.title("Login Form")

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack(pady=5)

        self.username_entry = tk.Entry(master)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack(pady=5)

        self.password_entry = tk.Entry(master, show='*')
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            messagebox.showinfo("Login", "Login Successful")
        else:
            messagebox.showerror("Login", "Invalid Credentials")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()