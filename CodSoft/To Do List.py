import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        # Task list
        self.tasks = []

        # Task entry
        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add task button
        add_button = tk.Button(master, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=5, pady=10)

        # Task listbox
        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, height=20, width=60)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Remove task button
        remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        remove_button.grid(row=2, column=0, padx=5, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)  # Clear the entry field
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)  # Clear the listbox
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
