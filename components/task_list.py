import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime

class TaskList(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.tasks = []  # List to store tasks

        # Task Input
        task_label = tk.Label(self, text="Task Name:", font=("Helvetica", 12))
        task_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.task_entry = tk.Entry(self, width=40)
        self.task_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Calendar widget for selecting deadlines
        deadline_label = tk.Label(self, text="Select Deadline:", font=("Helvetica", 12))
        deadline_label.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.calendar = Calendar(self, selectmode="day")
        self.calendar.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        # Add priority dropdown for tasks
        priority_label = tk.Label(self, text="Priority:", font=("Helvetica", 12))
        priority_label.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

        self.priority_var = tk.StringVar(self)
        self.priority_var.set("Medium")  # Default priority

        self.priority_dropdown = tk.OptionMenu(self, self.priority_var, "Low", "Medium", "High")
        self.priority_dropdown.grid(row=5, column=0, padx=10, pady=5, sticky="ew")

        # Add Task Button
        add_button = tk.Button(self, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        add_button.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

        # Task List Box
        self.task_listbox = tk.Listbox(self, height=10, width=50)
        self.task_listbox.grid(row=7, column=0, padx=10, pady=10, sticky="ew")

        # Load existing tasks from file
        self.load_tasks()

    def add_task(self):
        task_name = self.task_entry.get()
        deadline = self.calendar.get_date()
        priority = self.priority_var.get()

        if task_name == "":
            tk.messagebox.showwarning("Input Error", "Task name cannot be empty")
            return

        # Add task to internal list and display it
        task_info = f"{task_name} - Deadline: {deadline}, Priority: {priority}"
        self.tasks.append(task_info)
        self.task_listbox.insert(tk.END, task_info)

        # Save tasks to file
        self.save_tasks()

        # Clear the task entry field
        self.task_entry.delete(0, tk.END)

    def save_tasks(self):
        # Write tasks to a text file
        with open("logs/task_log.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def load_tasks(self):
        # Load tasks from the text file
        try:
            with open("logs/task_log.txt", "r") as file:
                tasks = file.readlines()
                for task in tasks:
                    self.task_listbox.insert(tk.END, task.strip())
                    self.tasks.append(task.strip())
        except FileNotFoundError:
            pass
