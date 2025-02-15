#learning the working of pyqt by making a basic age calculator


from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
import sys
from datetime import datetime

class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__() #we have overwritten the self method of the parent class (QWidget), so first we have to call 
                           #call the init of the parent method before overwriting and calling child class

        grid = QGridLayout()

        #create widgets
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()

        birthdate_label = QLabel("Date of Birth MM/DD/YYYY:")
        self.birthdate_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Age: ")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        #add widgets to the grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(birthdate_label, 1, 0)
        grid.addWidget(self.birthdate_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)#2row,0col, span across 1 row and both cols
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)#after creating the grid we have to set the grid to our class instance

    def calculate_age(self):
        current_year = datetime.now().year
        date_of_birth = self.birthdate_line_edit.text()

        #converting the year string into actual year
        year_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y").date().year
        age = current_year - year_of_birth
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old.")

        
app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())


