from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLineEdit, QLabel ,\
     QMainWindow, QTableWidget, QTableWidgetItem,QDialog, QVBoxLayout, \
     QComboBox, QPushButton, QWidget

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
        edit_menu = self.menuBar().addMenu("&Edit")

        add_student_action = QAction("Add Student", self)
        add_student_action.triggered.connect(self.add_student)
        file_menu.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu.addAction(about_action)
        # adding this line if we want to see the about action in
        # menu bar
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        search_action = QAction("Search", self)
        search_action.triggered.connect(self.search)
        edit_menu.addAction(search_action)


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

    def search(self):
        dialoge = SearchDialog()
        dialoge.exec()

    def add_student(self):
        dialoge = AddStudentDialog()
        dialoge.exec()

class AddStudentDialog(QDialog):
    def __init__(self, ) :
        super().__init__()

        self.setWindowTitle("Add Student")
        self.resize(400,400)

        layout = QVBoxLayout()

        # name widget

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Enter Name")
        layout.addWidget(self.student_name)

        # class widget
        self.student_class = QComboBox()
        classes = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII",
                   "IX", "X", "XI", "XII"]
        self.student_class.setPlaceholderText("Select Class")
        self.student_class.addItems(classes)
        layout.addWidget(self.student_class)
 
        # section widget
        self.student_section = QComboBox()
        sections = ["A", "B", "C", "D", "E"]
        self.student_section.setPlaceholderText("Select Section")
        self.student_section.addItems(sections)
        layout.addWidget(self.student_section)

        # phone number widget
        self.student_phone = QLineEdit()
        self.student_phone.setPlaceholderText("Enter Phone Number")
        self.student_phone.setInputMask('+91 00000 00000;_') # only 10 digits allowed
        layout.addWidget(self.student_phone)

        button = QPushButton("Register Student")
        button.clicked.connect(self.register_student)
        layout.addWidget(button)

        self.setLayout(layout)
        


    def register_student(self):
        name = self.student_name.text().strip().title()
        student_class = self.student_class.itemText(self.student_class.currentIndex())
        student_section = self.student_section.itemText(self.student_section.currentIndex())
        phone_number = self.student_phone.text().strip()

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (Name, Class, Section, 'Phone Number') VALUES (?,?,?,?)",
                       (name, student_class, student_section, phone_number))
        connection.commit()
        cursor.close()
        connection.close()
        window.load_data()
        self.close()

class SearchDialog(QDialog):
    def __init__(self, ):
        super().__init__()

        self.setWindowTitle("Search Student")
        self.resize(300,300)
        self.move(300,300)

        layout = QVBoxLayout()
        # input widget for search
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Student Name")
        layout.addWidget(self.search_input)

        #button widget
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_student)
        layout.addWidget(search_button)

        self.setLayout(layout)


    def search_student(self):
        name = self.search_input.text().strip().title()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        rows = cursor.execute("SELECT * FROM students WHERE Name LIKE ?",
                              (f"%{name}%",)).fetchall()
        
        if rows:
            items = window.table.findItems(name,Qt.MatchFlag.MatchContains)
            for item in items:
                window.table.item(item.row(), 1).setSelected(True)
        
        # clsoing the dialoge
        self.close()


app = QApplication(sys.argv)
window = StudentManagement()
window.show()
window.load_data()
sys.exit(app.exec())