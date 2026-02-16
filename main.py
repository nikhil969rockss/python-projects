from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLineEdit, QLabel ,\
     QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QAction
import sqlite3
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

        # creating the table for central widget

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(("ID", "Name", "Class",
                                              "Section", "Phone Number"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)


    def load_data(self):
        """This method is used to load the data and
        display it in the table widget"""
        
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        rows = cursor.execute("SELECT * FROM students").fetchall()
        # print(rows) # list of tuples

        self.table.setRowCount(0) # clear the table before populating it
        # populate the data to the table widget
        for row_number, row_data in enumerate(rows):
            self.table.insertRow(row_number)
            for coumn_number, data in enumerate(row_data):
                self.table.setItem(row_number, coumn_number,
                                   QTableWidgetItem(str(data)))
        
        cursor.close()
        connection.close()

app = QApplication(sys.argv)
window = StudentManagement()
window.show()
window.load_data()
sys.exit(app.exec())