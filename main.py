from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLineEdit ,\
     QMainWindow, QTableWidget, QTableWidgetItem,QDialog, QVBoxLayout, \
     QComboBox, QPushButton, QToolBar, QStatusBar, QGridLayout,QLabel, \
     QMessageBox

from PyQt6.QtGui import QAction, QIcon
import sqlite3
import sys    


class Database():
    def __init__(self, datbase_file= "database.db") :
        self.datbase_file = datbase_file

    def connect(self):
        connection = sqlite3.connect(self.datbase_file)
        return connection


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

        add_student_action = QAction(QIcon("icons/add.png"),"Add Student", self)
        add_student_action.triggered.connect(self.add_student)
        file_menu.addAction(add_student_action)

        about_action = QAction("About", self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)
        # adding this line if we want to see the about action in
        # menu bar
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        search_action = QAction(QIcon("icons/search.png"),"Search", self)
        search_action.triggered.connect(self.search)
        edit_menu.addAction(search_action)

        # creating the toolbar 
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)

        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        
        # creating the table for central widget

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(("ID", "Name", "Class",
                                              "Section", "Phone Number"))
        self.table.verticalHeader().setVisible(False)

        # making the table read only
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.setCentralWidget(self.table)

        # creating the status bar
        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        # display the button only if the cell is clicked
        # detect the cell clicked

        self.table.cellClicked.connect(self.cell_clicked)
        

    def load_data(self):
        """This method is used to load the data and
        display it in the table widget"""
        
        connection = Database().connect()
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

    def cell_clicked(self):
        edit_button = QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit_record)

        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete_record)

        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusBar().removeWidget(child)
        
        self.statusBar().addWidget(edit_button)
        self.statusBar().addWidget(delete_button)

    def edit_record(self):
        dialog = EditDialog()
        dialog.exec()
    
    def delete_record(self):
        dialog = DeleteDialog()
        dialog.exec()

    def about(self):
        dialog = AboutDialog()
        dialog.exec()


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

        connection = Database().connect()
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
        connection = Database().connect()
        cursor = connection.cursor()
        rows = cursor.execute("SELECT * FROM students WHERE Name LIKE ?",
                              (f"%{name}%",)).fetchall()
        
        if rows:
            items = window.table.findItems(name,Qt.MatchFlag.MatchContains)
            for item in items:
                window.table.item(item.row(), 1).setSelected(True)
        
        # clsoing the dialoge
        self.close()


class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Student Record")
        self.resize(300,300)
        self.move(800,300)

        layout = QVBoxLayout()
        
        
        # populate the existing data 
        index = window.table.currentRow()
        selected_student_name = window.table.item(index,1).text()
        selected_class = window.table.item(index, 2).text()
        selected_section = window.table.item(index, 3).text()
        selected_phone = window.table.item(index, 4).text()
        
        self.student_id = window.table.item(index,0).text()
        # name widget
        self.student_name = QLineEdit(selected_student_name)
        self.student_name.setPlaceholderText("Enter Name")
        layout.addWidget(self.student_name)

        # class widget
        self.student_class = QComboBox()
        classes = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII",
                   "IX", "X", "XI", "XII"]
        self.student_class.setPlaceholderText("Select Class")
        self.student_class.addItems(classes)
        self.student_class.setCurrentText(selected_class)
        layout.addWidget(self.student_class)
 
        # section widget
        self.student_section = QComboBox()
        sections = ["A", "B", "C", "D", "E"]
        self.student_section.setPlaceholderText("Select Section")
        self.student_section.addItems(sections)
        self.student_section.setCurrentText(selected_section)
        layout.addWidget(self.student_section)

        # phone number widget
        self.student_phone = QLineEdit(selected_phone)
        self.student_phone.setPlaceholderText("Enter Phone Number")
        self.student_phone.setInputMask('+91 00000 00000;_') # only 10 digits allowed
        layout.addWidget(self.student_phone)

        button = QPushButton("Update Student")
        button.clicked.connect(self.update_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def update_student(self):

        updated_name = self.student_name.text().strip().title()
        updated_class = self.student_class.itemText(self.student_class.currentIndex())
        updated_section = self.student_section.itemText(self.student_section.currentIndex())
        updated_phone = self.student_phone.text().strip()

        connection = Database().connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET Name=?, Class=?, Section=?, 'Phone Number'=? WHERE ID=?",
                       (updated_name,
                        updated_class,
                        updated_section,
                        updated_phone,
                        self.student_id))
        connection.commit()
        cursor.close()
        connection.close()
        window.load_data()
        self.close()


class DeleteDialog(QDialog):
    def __init__(self, ):
        super().__init__()
        self.setWindowTitle("Delete Student Record")
        
        layout = QGridLayout()
        message = QLabel("Are you sure you want to delete this record?")
        yess_button = QPushButton("Yes")
        yess_button.clicked.connect(self.delete_record)
        no_button = QPushButton("No")
        no_button.clicked.connect(self.close)

        layout.addWidget(message,0,0,1,2)
        layout.addWidget(yess_button, 1,0)
        layout.addWidget(no_button,1,1)

        self.setLayout(layout)


    def delete_record(self):
        index = window.table.currentRow()
        student_id = window.table.item(index,0).text()
        #db connection
        connection = Database().connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE ID=?", (student_id,))
        connection.commit()
        cursor.close()
        connection.close()
        window.load_data()

        success_message = QMessageBox()
        success_message.setWindowTitle("Success")
        success_message.setText("Record Deleted Successfully")
        success_message.exec()
        
        self.close()


class AboutDialog(QMessageBox):
    def __init__(self,):
        super().__init__()
        self.setWindowTitle("About Student Management App")
        self.setText("This is a simple student management application \
                     built using PyQt6 and SQLite. It allows you to add,\
                      edit, delete, and search for student records. \
                     The application is designed to be user-friendly \
                      and efficient for managing student information.")
        self.exec()

app = QApplication(sys.argv)
window = StudentManagement()
window.show()
window.load_data()
sys.exit(app.exec())
        
