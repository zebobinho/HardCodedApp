# Stress Management App

This application is designed to help users track their moods and manage tasks efficiently, contributing to overall stress management. The app features two main components: a **Mood Tracker** and a **Task List**, which are integrated into the main application to provide a seamless experience.

## Project Structure

The project directory is structured as follows:


/stress_management_app │ ├── app.py # Main file that runs the application ├── components │ ├── mood_tracker.py # File for mood tracker UI and logic │ └── task_list.py # File for task list UI and logic ├── logs # Directory for storing logs │ ├── mood_log.txt # Text file to store mood entries │ └── task_log.txt # Text file to store tasks and deadlines └── assets # Any images, icons, or other assets if needed
Key Components
app.py: This is the main entry point for the application. It coordinates the mood tracker and task list functionalities, allowing users to interact with both features seamlessly.


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
- **task_log.txt**: Stores all tasks with details such as deadlines and status.

### Assets

- A folder where any images, icons, or other assets can be placed.

## Installation and Setup

1. Clone the repository to your local machine:
   git clone <repository_url>
2. Install any necessary dependencies:
   pip install -r requirements.txt
3. Run the application:
   python App.py

## Usage
Mood Tracker: Track how you feel throughout the day and reflect on your emotions.
Task List: Organize your tasks and stay on top of your deadlines to reduce stress.
