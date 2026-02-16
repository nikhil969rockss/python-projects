from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLineEdit, QLabel ,\
     QMainWindow
from PyQt6.QtGui import QAction

import sys    


class StudentManagement(QMainWindow):
    def __init__(self, ):
        super().__init__()
        # setting up window title
        self.setWindowTitle("Student Management App")

        # setting up window resize 
        self.resize(600,400)

        # setting up menu items 

        file_menu = self.menuBar().addMenu("&File")
        help_menu = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student", self)
        file_menu.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu.addAction(about_action)
        # adding this line if we want to see the about action in
        # menu bar
        about_action.setMenuRole(QAction.MenuRole.NoRole)


app = QApplication(sys.argv)
window = StudentManagement()
window.show()
sys.exit(app.exec())