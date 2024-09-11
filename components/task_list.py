import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime

class TaskList(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app  # Store the reference to the main app

        self.tasks = []  # List to store tasks
        self.current_filter = 0  # 0 = Sort by due date, 1 = Sort by importance (priority)

        # Define colors
        self.bg_color = "light gray"
        self.text_color = "black"

        # Configure the grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(7, weight=1)

        # Task Input
        task_label = tk.Label(self, text="Task Name:", font=("Helvetica", 12), bg=self.bg_color, fg=self.text_color)
        task_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.task_entry = tk.Entry(self, width=40, bg=self.bg_color, fg=self.text_color)
        self.task_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Calendar widget for selecting deadlines
        deadline_label = tk.Label(self, text="Select Deadline:", font=("Helvetica", 12), bg=self.bg_color, fg=self.text_color)
        deadline_label.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        # Removing the week numbers in the calendar
        self.calendar = Calendar(self, selectmode="day", showweeknumbers=False)
        self.calendar.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        # Priority dropdown
        priority_label = tk.Label(self, text="Priority:", font=("Helvetica", 12), bg=self.bg_color, fg=self.text_color)
        priority_label.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

        self.priority_var = tk.StringVar(self)
        self.priority_var.set("Medium")  # Default priority

        self.priority_dropdown = tk.OptionMenu(self, self.priority_var, "Low", "Medium", "High")
        self.priority_dropdown.config(bg=self.bg_color, fg=self.text_color)
        self.priority_dropdown.grid(row=5, column=0, padx=10, pady=5, sticky="ew")

        # Add Task Button
        add_button = tk.Button(self, text="Add Task", command=self.add_task, bg="#4CAF50", fg="black", font=("Helvetica", 12))
        add_button.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

        # Task List Box
        self.task_listbox = tk.Listbox(self, height=10, width=50, bg=self.bg_color, fg=self.text_color)
        self.task_listbox.grid(row=7, column=0, padx=10, pady=10, sticky="nsew")

        # Sort by due date button
        sort_due_button = tk.Button(self, text="Sort by Due Date", command=self.sort_by_due_date, bg="#2196F3", fg="black", font=("Helvetica", 12))
        sort_due_button.grid(row=8, column=0, padx=10, pady=10, sticky="ew")

        # Sort by importance button
        sort_importance_button = tk.Button(self, text="Sort by Importance", command=self.sort_by_importance, bg="#FF5722", fg="black", font=("Helvetica", 12))
        sort_importance_button.grid(row=9, column=0, padx=10, pady=10, sticky="ew")

        # Back button using ttk and matching the style
        back_button = ttk.Button(self, text="Back to Main Menu", command=self.app.show_initial_screen, style='Custom.TButton')
        back_button.grid(row=10, column=0, padx=10, pady=10, sticky="ew")

        # Load tasks and refresh the task list
        self.load_tasks()
        self.update_idletasks()  # Force an immediate update
        self.task_entry.focus()  # Set focus on the task entry field

    def add_task(self):
        task_name = self.task_entry.get()
        deadline = self.calendar.get_date()  # Get the selected date as a string (e.g., '09/10/2024')
        priority = self.priority_var.get()

        if task_name == "":
            tk.messagebox.showwarning("Input Error", "Task name cannot be empty")
            return

        # Convert the deadline string into a datetime object for validation
        deadline_date = datetime.strptime(deadline, "%m/%d/%y")

        # Get the current date for comparison
        current_date = datetime.now()

        # Check if the selected date is in the past
        if deadline_date < current_date:
            tk.messagebox.showerror("Invalid Date", "The selected deadline has already passed. Please choose a future date.")
            return

        # Add the task to the internal list as a tuple (task_name, deadline, priority)
        task_info = (task_name, deadline_date, priority)
        self.tasks.append(task_info)

        # Clear the task entry field
        self.task_entry.delete(0, tk.END)

        # Refresh the task listbox and save tasks
        self.update_task_listbox()
        self.save_tasks()

    def save_tasks(self):
        # Write sorted tasks to a text file
        with open("logs/task_log.txt", "w") as file:
            for task in self.tasks:
                # Format each task for display and saving
                task_string = f"{task[0]} - Deadline: {task[1].strftime('%m/%d/%y')}, Priority: {task[2]}"
                file.write(f"{task_string}\n")

    def load_tasks(self):
        # Clear the current task list
        self.tasks.clear()

        # Load tasks from the text file
        try:
            with open("logs/task_log.txt", "r") as file:
                tasks = file.readlines()
                for task in tasks:
                    # Split the task string and extract the task name, deadline, and priority
                    task_name, rest = task.split(" - Deadline: ")
                    deadline_str, priority = rest.split(", Priority: ")

                    # Convert deadline string back to a datetime object
                    deadline_date = datetime.strptime(deadline_str.strip(), "%m/%d/%y")

                    # Append the task as a tuple (task_name, deadline_date, priority)
                    self.tasks.append((task_name, deadline_date, priority.strip()))
                
                # Update the task listbox after loading tasks
                self.update_task_listbox()
        except FileNotFoundError:
            pass

    def update_task_listbox(self):
        # Clear the listbox
        self.task_listbox.delete(0, tk.END)

        # Display the tasks in the listbox
        for task in self.tasks:
            task_string = f"{task[0]} - Deadline: {task[1].strftime('%m/%d/%y')}, Priority: {task[2]}"
            self.task_listbox.insert(tk.END, task_string)

    def sort_by_due_date(self):
        # Sort tasks by deadline
        self.tasks.sort(key=lambda task: task[1])
        self.current_filter = 0  # Set the current filter to "sort by due date"
        self.update_task_listbox()

    def sort_by_importance(self):
        # Define a priority mapping for sorting
        priority_map = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks.sort(key=lambda task: priority_map[task[2]])
        self.current_filter = 1  # Set the current filter to "sort by importance"
        self.update_task_listbox()
