# Stress Management App

This application is designed to help users track their moods and manage tasks efficiently, contributing to overall stress management. The app features two main components: a **Mood Tracker** and a **Task List**, which are integrated into the main application to provide a seamless experience.

## Project Structure

The project directory is structured as follows:


/stress_management_app<br>
│<br>
├── app.py                 # Main file that runs the application<br>
├── components<br>
│   ├── mood_tracker.py     # File for mood tracker UI and logic (handled by one student)<br>
│   └── task_list.py        # File for task list UI and logic (handled by the other student)<br>
├── logs                    # Directory for storing logs (new)<br>
│   ├── mood_log.txt        # Text file to store mood entries<br>
│   └── task_log.txt        # Text file to store tasks and deadlines<br>
└── assets                  # Any images, icons, or other assets if needed<br>


### Key Components

- **`app.py`**: This is the main entry point for the application. It coordinates the mood tracker and task list functionalities, allowing users to interact with both features seamlessly.
  
- **Mood Tracker (`mood_tracker.py`)**: 
  - Helps users log their daily moods.
  - Mood entries are saved in the `logs/mood_log.txt` file.
  
- **Task List (`task_list.py`)**: 
  - Allows users to create and manage tasks, set deadlines, and keep track of task progress.
  - Task entries are saved in the `logs/task_log.txt` file.

### Logs

- **mood_log.txt**: Stores all mood entries with timestamps.
- **task_log.txt**: Stores all tasks with details such as task name, task due date and importance.

### Assets

- A folder where any images, icons, or other assets can be placed.

## Installation and Setup

1. Clone the repository to your local machine:
   git clone https://github.com/zebobinho/HardCodedApp
2. Install any necessary dependencies:
   pip install -r requirements.txt
3. Run the application:
   python App.py

## Usage
Mood Tracker: Track how you feel throughout the day and reflect on your emotions.<br>

### Overview 
Task List: Organize your tasks and stay on top of your deadlines to reduce stress and provides assistance on how to approach your tasks.<br>
### Components
#### Task Creation
The task list is made up the **`Task Name`**, **`Calendar`**, **`Importance`** and **`Add Task`** which are all used for the user to create their tasks. <br>
#### Filters
The box in the middle of the screen is where the tasks will be displayed, to enhance the display of tasks, there are 3 filters that can be used to see your tasks in different ways:<br>
- **`Sort by Due Data`** to see tasks from the closest due date to the furthest due date
- **`Sort by Importance`** to see tasks from High importance to Low importance


