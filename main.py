import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem
from PyQt5 import uic, QtCore
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("main.ui", self)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
    def calendarDateChanged(self):
        print("The calendar date was changed")
        dateSelected = self.calendarWidget.selectedDate().toPyDate().strftime("%d/%m/%Y")
        print("selected date: ", dateSelected)
        self.updateTaskList(dateSelected)

    def updateTaskList(self,date):
        self.tasksListWidget.clear()
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        query = "SELECT task , completed FROM tasks where date=?"
        row = (date,)
        results = cursor.execute(query,row).fetchall()
        for result in results:
            item = QListWidgetItem(str(result[0]))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.tasksListWidget.addItem(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
