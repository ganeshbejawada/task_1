#TASK 1
#TO-DO List

import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        # Initialize tasks list
        self.tasks = []
        
        # Create GUI elements
        self.header_label = tk.Label(self.root, text="Welcome to To-Do List App", font=("Helvetica", 16, "bold"), pady=10, fg="blue")
        self.header_label.pack()
        
        self.task_listbox = tk.Listbox(self.root, width=60, height=10, font=("Helvetica", 12))
        self.task_listbox.pack(pady=20)
        
        self.menu_label = tk.Label(self.root, text="Select an option:", font=("Helvetica", 12))
        self.menu_label.pack()
        
        self.add_button = tk.Button(self.root, text="Add Task", width=20, command=self.add_task, bg="green", fg="white")
        self.add_button.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.complete_button = tk.Button(self.root, text="Mark Complete", width=20, command=self.mark_complete, bg="blue", fg="white")
        self.complete_button.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.delete_button = tk.Button(self.root, text="Delete Task", width=20, command=self.delete_task, bg="red", fg="white")
        self.delete_button.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.exit_button = tk.Button(self.root, text="Exit", width=20, command=self.root.quit)
        self.exit_button.pack(pady=10)
        
        # Load tasks from file
        self.load_tasks()
        self.update_task_listbox()
    
    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter task:")
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.save_tasks()
    
    def mark_complete(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index]["completed"] = True
            self.update_task_listbox()
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")
    
    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.update_task_listbox()
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_name = f"[{'X' if task['completed'] else ' '}] {task['task']}"
            self.task_listbox.insert(tk.END, task_name)
    
    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(f"{task['task']},{task['completed']}\n")
    
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                for line in f:
                    task_info = line.strip().split(',')
                    self.tasks.append({"task": task_info[0], "completed": task_info[1] == "True"})
        except FileNotFoundError:
            pass  # No saved tasks yet

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
