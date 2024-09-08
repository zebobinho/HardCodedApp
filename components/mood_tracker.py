import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class MoodTracker(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app  # Store the reference to the main app

        label = tk.Label(self, text="How are you feeling today?", font=("Helvetica", 16), pady=10)
        label.grid(row=0, column=0, columnspan=3)

        emotions = [
            {"name": "Happy", "emoji": "😊"},
            {"name": "Sad", "emoji": "😢"},
            {"name": "Angry", "emoji": "😠"},
            {"name": "Excited", "emoji": "😃"},
            {"name": "Tired", "emoji": "😴"},
            {"name": "Stressed", "emoji": "😖"},
        ]

        self.emotion_buttons = []
        for idx, emotion in enumerate(emotions):
            button = tk.Button(self, text=f"{emotion['emoji']}\n{emotion['name']}", width=12, height=4)
            button.grid(row=idx // 3 + 1, column=idx % 3, padx=15, pady=10)
            self.emotion_buttons.append(button)
            button.config(command=lambda e=emotion, btn=button: self.select_mood(e['name'], btn))

        journal_label = tk.Label(self, text="Journal your feelings (optional, max 100 words):", pady=5)
        journal_label.grid(row=4, column=0, columnspan=3)

        self.journal_entry = tk.Text(self, height=5, width=35, wrap='word', bg="#f9f9f9")
        self.journal_entry.grid(row=5, column=0, columnspan=3, padx=10, pady=5)

        self.submit_button = tk.Button(self, text="Submit", state='disabled', bg="#d0d0d0", relief="flat", font=("Helvetica", 12))
        self.submit_button.grid(row=6, column=0, columnspan=3, pady=10)

        # Back button
        back_button = tk.Button(self, text="Back to Main Menu", command=self.app.show_initial_screen, font=("Helvetica", 12))
        back_button.grid(row=7, column=0, columnspan=3, pady=10)

        self.previous_entries_box = tk.Text(self, height=10, width=40, state='disabled', bg="#f9f9f9")
        self.previous_entries_box.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

        self.load_previous_entries()

    def select_mood(self, mood, button):
        self.selected_mood = mood

        # Reset all buttons to default color
        for b in self.emotion_buttons:
            b.config(bg="SystemButtonFace")

        # Highlight the selected button
        button.config(bg="lightgray")

        # Enable submit button
        self.submit_button.config(state='normal', bg="blue")

    def submit_mood(self):
        if self.selected_mood:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            journal_text = self.journal_entry.get("1.0", "end").strip()
            journal_text = journal_text[:500]  # Limit to 100 words (500 characters approx.)

            # Log to file in the 'logs' directory
            with open("logs/mood_log.txt", "a") as f:
                f.write(f"{current_time} - Mood: {self.selected_mood}\n")
                if journal_text:
                    f.write(f"Journal: {journal_text}\n")
                f.write("\n")

            # Update previous entries display
            self.previous_entries_box.config(state='normal')
            self.previous_entries_box.insert(tk.END, f"{current_time} - Mood: {self.selected_mood}\n")
            if journal_text:
                self.previous_entries_box.insert(tk.END, f"Journal: {journal_text}\n")
            self.previous_entries_box.insert(tk.END, "\n")
            self.previous_entries_box.config(state='disabled')

            # Clear journal entry and reset mood
            self.journal_entry.delete("1.0", "end")
            self.selected_mood = None
            self.submit_button.config(state='disabled', bg="#d0d0d0")

    def load_previous_entries(self):
        try:
            with open("logs/mood_log.txt", "r") as f:
                previous_entries = f.read()
                self.previous_entries_box.config(state='normal')
                self.previous_entries_box.insert(tk.END, previous_entries)
                self.previous_entries_box.config(state='disabled')
        except FileNotFoundError:
            pass
