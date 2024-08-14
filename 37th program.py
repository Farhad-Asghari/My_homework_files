# Create a class ToDo that uses tkinter to create a to-do list GUI where usres can add and remove tasks.
import tkinter as tk
root = tk.Tk()
root.title = ("ToDolist App")
tasks = []
def add_task():
    task = entry.get()
    if task:
        task.append(task)
        task_list.inseert(tk,END, task)
        entery.delete(0,tk.END)

def remove_task():
    selection = task_list.curselection()
    if selection:
        index = selection[0]
        task_list.delete(index) 
        del tasks[index]

entery = tk.Entry(root, width=30)
entery.pack(pady=10)
add_button = tk.Button(root,text = "add task", command=add_task)
add_button.pack(pady=5)
task_list = tk.Listbox(root, height=10, width=50)
task_list.pack(pady=10)
remove_button = tk.Button(root, text="delete task", command=remove_task)
remove_button.pack(pady=5)
root.mainloop()
        