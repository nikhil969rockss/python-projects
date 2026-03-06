
from PyQt6.QtWidgets import QGridLayout, QLabel, QPushButton , \
     QWidget, QApplication, QLineEdit

from datetime import datetime
import sys

class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Age Calculator")

        grid = QGridLayout()
        # making widgets

        name_label = QLabel("Name:")
        self.name_input = QLineEdit()

        birth_year_label = QLabel("Enter Date of Birth (dd/mm/yy):")
        self.birth_year_input = QLineEdit()

        button = QPushButton("Calculate Age")
        button.clicked.connect(self.calc_age)

        self.output_label = QLabel("")

        # adding widegts to the layout

        grid.addWidget(name_label,0,0 )
        grid.addWidget(self.name_input,0,1 )
        grid.addWidget(birth_year_label,1,0 )
        grid.addWidget(self.birth_year_input,1,1 )
        grid.addWidget(button,2,0,1,2)
        grid.addWidget(self.output_label,3,0,1,2)


        self.setLayout(grid)


    def calc_age(self):
        current_year = datetime.now().year
        user_name = self.name_input.text()
        birth_date = self.birth_year_input.text()
        user_date_year = datetime.strptime(birth_date, "%d/%m/%Y").year

        age = current_year - user_date_year

        self.output_label.setText(f"Age of {user_name} is {age} years old")


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())