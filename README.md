# Daily Task Manager

A simple PyQt5 application to manage daily tasks using a calendar widget and a list view. Tasks can be added, edited, and marked as completed. The application uses SQLite for data storage.

## Features

- **Calendar Integration**: Select a date to view tasks for that day.
- **Task Management**: Add, edit, and delete tasks.
- **Task Status**: Mark tasks as completed or incomplete with color-coded backgrounds.
- **Data Storage**: Uses SQLite database to store tasks.

## Requirements

- Python 3.11
- PyQt5
- SQLite3

## Installation

1. **Clone the repository:**

    ```bash
    git clone <https://github.com/yakupzengin/daily-task-manager>
    cd <daily-task-manager>
    ```

2. **Install dependencies:**

    Make sure you have Python installed. Then install PyQt5 using pip:

    ```bash
    pip install pyqt5
    ```

3. **Setup the database:**

    Ensure that the SQLite database (`data.db`) is created with the appropriate schema. You can create it manually or use a script if provided in the repository.

## Usage

1. **Run the Application:**

    Execute the main script to start the application:

    ```bash
    python main.py
    ```

2. **Interface Overview:**

    - **Calendar Widget**: Select a date to view and manage tasks.
    - **Task List Widget**: Displays tasks for the selected date. Tasks can be checked as completed or incomplete.
    - **Add Task**: Use the `Add task` button to create new tasks.
    - **Edit Task**: Double-click a task to edit its details.

## Code Description

- **`main.py`**: Main application logic. Handles task management, calendar integration, and interaction with the SQLite database.
- **`edit_task.py`**: Contains the `EditTaskDialog` class for editing tasks.
- **`main.ui`**: Qt Designer UI file for the main window.
- **`edit_task.ui`**: Qt Designer UI file for the edit task dialog.