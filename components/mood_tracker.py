import tkinter as tk
from datetime import datetime

class MoodTracker(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Your mood tracker initialization logic
        self.selected_mood = None
        self.selected_button = None

        # Header for mood tracker
        label = tk.Label(self, text="How are you feeling today?", font=("Helvetica", 26), pady=10)
        label.grid(row=0, column=0, columnspan=3)

        # Emojis for emotions
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
            button.config(command=lambda e=emotion, btn=button: self.select_mood(e['name'], btn))
            self.emotion_buttons.append(button)

        # Journal text box
        journal_label = tk.Label(self, text="Journal your feelings (optional, max 100 words):", pady=5)
        journal_label.grid(row=4, column=0, columnspan=3)

        self.journal_entry = tk.Text(self, height=5, width=35, wrap='word', bg="#f9f9f9")
        self.journal_entry.grid(row=5, column=0, columnspan=3, padx=10, pady=5)

        # Log button (centered)
        self.log_button = tk.Button(self, text="Log", width=20, height=2, state='disabled', bg="#4CAF50",
                                    fg="black", font=("Helvetica", 12), command=self.log_only)
        self.log_button.grid(row=6, column=0, columnspan=3, pady=10)

        # Wipe button
        self.wipe_button = tk.Button(self, text="Wipe Advice", width=20, height=2, bg="#4CAF50", fg="black", font=("Helvetica", 12), command=self.wipe_advice)
        self.wipe_button.grid(row=8, column=0, columnspan=3, pady=10)

        # Previous Logs button
        self.previous_logs_button = tk.Button(self, text="Previous Logs", width=20, height=2, bg="#4CAF50", fg="black",
                                              font=("Helvetica", 12), command=self.show_previous_logs)
        self.previous_logs_button.grid(row=9, column=0, columnspan=3, pady=10)

        # Box to show advice (hardcoded responses, increased size and added border)
        self.advice_box = tk.Text(self, height=10, width=50, wrap="word", state='disabled', bg="#f9f9f9", borderwidth=2, relief="solid")
        self.advice_box.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

        # Load previous entries from file
        self.load_previous_entries()
