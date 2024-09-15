import tkinter as tk
from datetime import datetime

class MoodTracker(tk.Frame):
    def _init_(self, master):
        super()._init_(master)

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

    def select_mood(self, mood, button):
        self.selected_mood = mood

        # Reset all buttons
        for b in self.emotion_buttons:
            b.config(bg="SystemButtonFace")

        # Highlight selected button
        button.config(bg="lightgray")

        # Enable buttons
        self.log_button.config(state='normal', bg="blue")

    def log_only(self):
        """Logs mood and journal entry to the file and provides hardcoded advice."""
        if self.selected_mood:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            journal_text = self.journal_entry.get("1.0", "end").strip()

            # Log the mood and journal entry
            with open("logs/mood_log.txt", "a") as f:
                f.write(f"{current_time} - Mood: {self.selected_mood}\n")
                if journal_text:
                    f.write(f"Journal: {journal_text}\n")
                f.write("\n")

            # Provide hardcoded advice based on selected mood
            advice = self.get_hardcoded_advice(self.selected_mood)

            # Display advice in the advice box
            self.advice_box.config(state='normal')
            self.advice_box.delete("1.0", "end")  # Clear previous advice
            self.advice_box.insert("end", advice)
            self.advice_box.config(state='disabled')

            # Clear journal entry
            self.journal_entry.delete("1.0", "end")
            self.log_button.config(state='disabled', bg="#d0d0d0")

    def get_hardcoded_advice(self, mood):
        """Returns a hardcoded response based on the selected mood."""
        responses = {
            "Happy": "It's great that you're feeling happy! Keep spreading positive vibes and remember to appreciate the little things in life that bring you joy.",
            "Sad": "It's okay to feel sad sometimes. Allow yourself to process these feelings. Reach out to someone you trust and talk it through.",
            "Angry": "Anger is a normal emotion. Try to take deep breaths and give yourself some space to cool down before reacting.",
            "Excited": "Excitement can be a wonderful motivator! Channel this energy into something productive and enjoy the moment to the fullest.",
            "Tired": "It sounds like you're feeling tired. Make sure you're taking enough breaks and getting plenty of rest. Sleep is essential for mental clarity.",
            "Stressed": "Stress can be overwhelming, but remember to take things one step at a time. Prioritize tasks and don't hesitate to ask for help if you need it."
        }
        return responses.get(mood, "No advice available for this mood.")

    def wipe_advice(self):
        """Clear the advice box."""
        self.advice_box.config(state='normal')
        self.advice_box.delete("1.0", "end")
        self.advice_box.config(state='disabled')

    def show_previous_logs(self):
        """Opens a new window to show the previous mood logs."""
        log_window = tk.Toplevel(self)
        log_window.title("Previous Logs")
        log_window.geometry("600x400")

        text_widget = tk.Text(log_window, wrap="word")
        text_widget.pack(fill="both", expand=True)

        try:
            with open("logs/mood_log.txt", "r") as f:
                logs = f.read()
                text_widget.insert("1.0", logs)
        except FileNotFoundError:
            text_widget.insert("1.0", "No logs found.")

        text_widget.config(state='disabled')  # Make text read-only

    def load_previous_entries(self):
        try:
            with open("logs/mood_log.txt", "r") as f:
                previous_entries = f.read()
                print(previous_entries)  # For debugging purposes
        except FileNotFoundError:
            pass