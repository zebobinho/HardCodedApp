import os
import tkinter as tk
from tkinter import ttk
from components.task_list import TaskList
from components.mood_tracker import MoodTracker
from PIL import Image, ImageTk

class StressManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Stress Management App")
        self.geometry("525x900+300+100")
        
        # Configure button styles
        self.style = ttk.Style(self)
        self.style.configure('TButton', font=('Helvetica', 12))
        self.style.configure('Custom.TButton', foreground='dark gray', background='light gray')

        # Initial screen
        self.container = ttk.Frame(self)
        self.container.pack(fill='both', expand=True)
        
        self.show_initial_screen()

    def show_initial_screen(self):
        # Clear previous content
        for widget in self.container.winfo_children():
            widget.destroy()
        
        # Dynamically build the file path to the image
        current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current script's directory
        image_path = os.path.join(current_dir, "assets", "StressApp.png")

        # Add the image in the center
        try:
            img = Image.open(image_path)
            img = img.resize((500, 500), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
        
            img_label = ttk.Label(self.container, image=photo)
            img_label.image = photo  # Keep a reference to avoid garbage collection
            img_label.place(relx=0.5, rely=0.4, anchor='center')
        except Exception as e:
            print(f"Error loading image: {e}")
            img_label = ttk.Label(self.container, text="Image not found", font=("Arial", 20))
            img_label.place(relx=0.5, rely=0.4, anchor='center')

        # Add buttons for navigation
        task_button = ttk.Button(self.container, text="Task List", command=self.show_task_list, style='Custom.TButton')
        task_button.place(relx=0, rely=0.9, relwidth=0.5, anchor='w')  # Left half

        mood_button = ttk.Button(self.container, text="Mood Tracker", command=self.show_mood_tracker, style='Custom.TButton')
        mood_button.place(relx=1, rely=0.9, relwidth=0.5, anchor='e')  # Right half

    def show_task_list(self):
        for widget in self.container.winfo_children():
            widget.destroy()
        
        task_list_frame = TaskList(self.container, self)  # Pass self (the main app)
        task_list_frame.pack(fill='both', expand=True)

    def show_mood_tracker(self):
        for widget in self.container.winfo_children():
            widget.destroy()
        
        mood_tracker_frame = MoodTracker(self.container, self)  # Pass self (the main app)
        mood_tracker_frame.pack(fill='both', expand=True)


if __name__ == "__main__":
    app = StressManagementApp()
    app.mainloop()
