import sqlite3
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QMessageBox
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtGui import QColor  # QColor is imported to set item background colors
import sys
from edit_task import EditTaskDialog

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("main.ui", self)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.saveChanges)
        self.addButton.clicked.connect(self.addNewTask)
        self.tasksListWidget.clicked.connect(self.saveChanges)
        self.tasksListWidget.itemDoubleClicked.connect(self.EditTask)

    def calendarDateChanged(self):
        print("The calendar date was changed")
        dateSelected = self.calendarWidget.selectedDate().toPyDate().strftime("%d/%m/%Y")
        print("selected date: ", dateSelected)
        self.updateTaskList(dateSelected)

    def updateTaskList(self, date):
        self.tasksListWidget.clear()
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        query = "SELECT task, completed FROM tasks WHERE date=?"
        row = (date,)
        results = cursor.execute(query, row).fetchall()

        if not results:  # If no tasks are found
            print("No tasks found for the selected date.")
            return

        for result in results:
            item = QListWidgetItem(str(result[0]))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            if result[1] == "YES":
                item.setCheckState(QtCore.Qt.Checked)
                item.setBackground(QColor(60, 179, 113))  # Green background for completed tasks
            else:
                item.setCheckState(QtCore.Qt.Unchecked)
                item.setBackground(QColor(184, 224, 255))  # Light blue background for incomplete tasks

            self.tasksListWidget.addItem(item)

    def saveChanges(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        date = self.calendarWidget.selectedDate().toPyDate().strftime("%d/%m/%Y")
        for i in range(self.tasksListWidget.count()):
            item = self.tasksListWidget.item(i)
            task = item.text()
            if item.checkState() == QtCore.Qt.Checked:
                item.setBackground(QColor(60, 179, 113))  # Green background for completed tasks
                query ="UPDATE tasks SET completed = 'YES' WHERE task = ? AND date=?"
            else:
                item.setBackground(QColor(184, 224, 255))  # Light blue background for incomplete tasks
                query ="UPDATE tasks SET completed = 'NO' WHERE task = ? AND date=?"

            row = (task, date,)
            cursor.execute(query, row)
        db.commit()

        print("db.commit()")
        messageBox = QMessageBox(self)
        messageBox.setWindowTitle("Task Manager")
        messageBox.setText("Changes have been successfully saved.")
        messageBox.setIcon(QMessageBox.Information)
        messageBox.setStandardButtons(QMessageBox.Ok)

        # Apply custom styles to the message box
        messageBox.setStyleSheet("""
            QMessageBox {
                background-color: #f0f0f0;  /* Background color */
                font-family: Arial;         /* Font */
                font-size: 14px;            /* Font size */
            }
            QMessageBox QLabel {
                color: #333333;             /* Text color */
            }
            QPushButton {
                background-color: rgb(25, 126, 19);  /* Button background color */
                color: white;               /* Button text color */
                padding: 6px 12px;          /* Button padding */
                border-radius: 4px;         /* Button border radius */
                transition: all 0.3s ease;  /* Hover animation */
            }
            QPushButton:hover {
                background-color: rgb(25, 88, 19);  /* Button hover color */
                transform: scale(1.05);     /* Scale effect on hover */
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);  /* Hover shadow effect */
                cursor: wait;               /* Cursor on hover */
            }
        """)

        messageBox.exec_()

    def addNewTask(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        newTask = str(self.taskLineEdit.text())
        date = self.calendarWidget.selectedDate().toPyDate().strftime("%d/%m/%Y")
        query = "INSERT INTO tasks(task, completed, date) VALUES(?, ?, ?)"
        row = (newTask, "NO", date)
        cursor.execute(query, row)
        db.commit()
        self.updateTaskList(date)
        self.taskLineEdit.clear()

    def EditTask(self, item):
        str(self.tasksListWidget.currentItem().text())
        currentItem = self.tasksListWidget.currentItem()
        task_text = str(currentItem.text())
        print("task_text", task_text)
        date = self.calendarWidget.selectedDate().toPyDate().strftime("%d/%m/%Y")
        # Open the EditTaskDialog with the selected task text
        dialog = EditTaskDialog(task_text, parent=self)


        if dialog.exec_():
            # If the user confirms the edit, update the task list
            updatedTask = dialog.saveChanges()
            self.updateTaskInDatabase(task_text,updatedTask,date)
            self.updateTaskList(date)

    def updateTaskInDatabase(self, task_text,new_task_text,date):
        print("old task :", task_text)
        print("new task :", new_task_text)
        print("date :" , date)
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        query = "UPDATE tasks SET task=? WHERE task=? AND date=?"
        cursor.execute(query, (new_task_text, task_text, date))
        db.commit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
