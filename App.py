import tkinter as tk
from components.mood_tracker import MoodTracker
from components.task_list import TaskList

class StressManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set fixed window size and center the window on the screen
        self.title("Stress Management App")
        self.geometry("525x900+300+100")  # Fixed window size, centered on screen (adjust +300+100 if needed)
        

        # Create frames for Mood Tracker and Task List
        self.mood_tracker_frame = MoodTracker(self)
        self.task_list_frame = TaskList(self)

        # Show the mood tracker by default
        self.mood_tracker_frame.pack(fill="both", expand=True)

        # Create a menu bar at the bottom
        self.create_menu_bar()

    def create_menu_bar(self):
        # Frame for the menu buttons at the bottom
        menu_bar = tk.Frame(self, height=50, bg="gray")
        menu_bar.pack(side="bottom", fill="x")

        # Button to switch to Mood Tracker
        mood_button = tk.Button(menu_bar, text="Mood Tracker", command=self.show_mood_tracker)
        mood_button.pack(side="left", expand=True, fill="both")

        # Button to switch to Task List
        task_button = tk.Button(menu_bar, text="Task List", command=self.show_task_list)
        task_button.pack(side="right", expand=True, fill="both")

    def show_mood_tracker(self):
        # Hide task list and show mood tracker
        self.task_list_frame.pack_forget()
        self.mood_tracker_frame.pack(fill="both", expand=True)

    def show_task_list(self):
        # Hide mood tracker and show task list
        self.mood_tracker_frame.pack_forget()
        self.task_list_frame.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = StressManagementApp()
    app.mainloop()
