import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class EditTaskDialog(QtWidgets.QDialog):
    def __init__(self, task_text, parent=None):
        super(EditTaskDialog, self).__init__(parent)
        self.setWindowTitle("Edit Task")
        self.setGeometry(100, 100, 300, 150)

        # Create layout
        self.layout = QtWidgets.QVBoxLayout(self)

        # Create and add widgets to the layout
        self.taskLineEdit = QtWidgets.QLineEdit(self)
        self.taskLineEdit.setPlaceholderText("Enter task details")
        self.taskLineEdit.setText(task_text)
        self.layout.addWidget(self.taskLineEdit)

        # Create button layout
        self.buttonLayout = QtWidgets.QHBoxLayout()

        self.saveButton = QtWidgets.QPushButton("Save", self)
        self.cancelButton = QtWidgets.QPushButton("Cancel", self)
        self.buttonLayout.addWidget(self.saveButton)
        self.buttonLayout.addWidget(self.cancelButton)

        self.layout.addLayout(self.buttonLayout)

        # Connect buttons to actions
        self.saveButton.clicked.connect(self.saveChanges)
        self.cancelButton.clicked.connect(self.reject)

    def saveChanges(self):
        new_task_text = self.taskLineEdit.text()
        print("new_task_text :",new_task_text)
        self.accept()
        return new_task_text

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     # Example task with existing text and priority
#     window = EditTaskDialog(task_text="Sample Task")
#     window.exec_()
#     sys.exit(app.exec_())
