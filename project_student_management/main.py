from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QComboBox, QToolBar, QStatusBar, QMessageBox
import sys
from PyQt6.QtGui import QAction, QIcon
import sqlite3
from PyQt6.QtCore import Qt


#this time we are using QMainWindow class because it helps to add tool bar, status bar and menu bar
#so use QMainWindow for bigger apps
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(800, 600)

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        #add sub-menu for file menu
        add_student_action = QAction(QIcon("project_student_management/icons/add.png"),"Add Student", self)
        add_student_action.triggered.connect(self.insert)

        file_menu_item.addAction(add_student_action)

        #search sub-menu for file menu
        search_action = QAction(QIcon("project_student_management/icons/search.png"),"Search Student", self)
        search_action.triggered.connect(self.search)

        file_menu_item.addAction(search_action)

        #about sub-menu for help menu
        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        about_action.triggered.connect(self.about)


        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        # Create toolbar and toolbar elements
        tool_bar = QToolBar()
        tool_bar.setMovable(True)
        self.addToolBar(tool_bar)

        tool_bar.addAction(add_student_action)
        tool_bar.addAction(search_action)

        # Create statusbar and statusbar elements
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        #Detect a cell click
        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        edit_button = QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete)

        children = self.findChildren(QPushButton) # so that buttons do not keep generating
        if children:
            for child in children:
                self.status_bar.removeWidget(child)

        self.status_bar.addWidget(edit_button)
        self.status_bar.addWidget(delete_button)


    def load_data(self):
        connection = sqlite3.connect("project_student_management/database.db")
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number) #creating an empty row
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))#filling the row with information

        connection.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()
    def search(self):
        dialog = SearchDialog()
        dialog.exec()
    def edit(self):
        dialog = EditDialog()
        dialog.exec()
    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()
    def about(self):
        dialog = AboutDialog()
        dialog.exec()


class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        content = """
        The creator of this Application is Satvik Nanda, feel free to modify and use this app.
        """
        self.setText(content)


class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Student Data")
        self.setFixedHeight(500)
        self.setFixedWidth(500) #this is a good practice for pop-up windows

        layout = QVBoxLayout()

        index = main_window.table.currentRow()
        #get id for student
        self.student_id = main_window.table.item(index, 0).text()

        student_name = main_window.table.item(index, 1).text() #index row and 1st col
        

        # add studentname widget
        self.student_name = QLineEdit(student_name)
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # add combo box of courses
        course_name = main_window.table.item(index, 2).text() #now second col
        self.course_name = QComboBox()
        courses = ["Biology", "Maths", "Physics", "Astronomy"]
        self.course_name.addItems(courses)

        self.course_name.setCurrentText(course_name)
        layout.addWidget(self.course_name)

        #Add mobile widget
        mobile = main_window.table.item(index, 3).text()
        self.mobile = QLineEdit(mobile)
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        #add submit button
        button = QPushButton("Update?")
        button.clicked.connect(self.update_student)
        layout.addWidget(button)


        self.setLayout(layout)

    def update_student(self):
        connection = sqlite3.connect("project_student_management/database.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name = ?, course = ?, mobile = ? WHERE id = ?",
                        (self.student_name.text(), 
                         self.course_name.itemText(self.course_name.currentIndex()),
                         self.mobile.text(), 
                         self.student_id)
                      )

        connection.commit()
        cursor.close()
        connection.close()
        #Refresh the table
        main_window.load_data()

class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Student Data")

        layout = QGridLayout()
        confirmation = QLabel("Are you sure about deleting?")
        yes = QPushButton("yes")
        no = QPushButton("no")

        layout.addWidget(confirmation, 0, 0, 1, 2)#row 0, col 0, expanding 1 row, expanding 2 col
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)
        self.setLayout(layout)

        yes.clicked.connect(self.delete_student)

    
    def delete_student(self):
        index = main_window.table.currentRow()
        #get id for student
        student_id = main_window.table.item(index, 0).text()

        connection = sqlite3.connect("project_student_management/database.db")
        cursor = connection.cursor()
        cursor.execute("DELETE from students WHERE id = ?", (student_id, ))
        connection.commit()
        cursor.close()
        connection.close()
        #Refresh the table
        main_window.load_data()

        self.close()

        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle("Success")
        confirmation_widget.setText("The record was deleted successfully!")

        confirmation_widget.exec()



class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedHeight(500)
        self.setFixedWidth(500) #this is a good practice for pop-up windows

        layout = QVBoxLayout()

        # add studentname widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # add combo box of courses
        self.course_name = QComboBox()
        courses = ["Biology", "Maths", "Physics", "Astronomy"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        #Add mobile widget
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        #add submit button
        button = QPushButton("Register")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)


        self.setLayout(layout)
    
    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text()

        connection = sqlite3.connect("project_student_management/database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name,course,mobile) VALUES (?,?,?)", (name,course,mobile))

        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()

class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        #set window title and size
        self.setWindowTitle("Search student")
        self.setFixedHeight(300)
        self.setFixedWidth(300)

        #create layout and input window
        layout = QVBoxLayout()
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)
        layout.addWidget(self.student_name)

        #create button
        button = QPushButton("Search")
        button.clicked.connect(self.search)
        layout.addWidget(button)

        self.setLayout(layout)

    def search(self):
        name = self.student_name.text()
        connection = sqlite3.connect("project_student_management/database.db")
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        rows = list(result)
        print(rows)
        items = main_window.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            print(item)
            main_window.table.item(item.row(), 1).setSelected(True)

        cursor.close()
        connection.close()










app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())
