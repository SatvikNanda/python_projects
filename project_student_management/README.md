# Overview:<br>
The Student Management System is a Python-based desktop application built using PyQt6 and SQLite. It provides a user-friendly interface for managing student records, including functionalities to add, update, delete, and search for student details. The application demonstrates the integration of a relational database with an interactive GUI, making it a suitable project for educational and small-scale administrative purposes.<br>

# Features:<br>
1. Add Student: Register a new student by entering their name, course, and mobile number.<br>
2. Search Student: Quickly find a student using their name.<br>
3. Edit Student Details: Update existing student information such as name, course, or mobile number.<br>
4. Delete Student Record: Remove a student's record from the database.<br>

5. Interactive GUI:<br>
a. Menu bar with "File" and "Help" menus.<br>
b. Toolbar for quick access to actions like adding or searching for students.<br>
c. Status bar for displaying additional actions when a table cell is selected.<br><br>
6. Database Integration: All student data is stored and managed in an SQLite database.<br>
7. Error Handling: User-friendly dialogs for operations and confirmations.<br><br>

## Methodology:
#### Technologies Used:

1. PyQt6: For designing the graphical user interface.

2. SQLite: For storing and managing student records.

#### Code Structure:

a. MainWindow: The main class handling the application’s primary interface, including menus, toolbar, and table view.

b. Dialog classes (InsertDialog, EditDialog, DeleteDialog, SearchDialog): Modular dialogs for performing specific tasks.

c. AboutDialog: Displays information about the application.

#### Application Workflow:

On launching, the application connects to the SQLite database and fetches existing student data to display in a table.

Users can perform CRUD (Create, Read, Update, Delete) operations via the menu, toolbar, or interactive dialogs.

Changes in the database are immediately reflected in the table view.<br><br>

## Output:
The Student Management System provides a clear and interactive interface with the following output components:

#### Student Table: 
Displays student records in a tabular format with columns for ID, Name, Course, and Mobile.

#### Dialogs:

Add Student: Allows users to input details and register a student.

Edit Student: Opens a dialog pre-filled with the selected student's information for editing.

Delete Student: Prompts a confirmation dialog before deleting a record.

Search Student: Highlights the matching student in the table view based on the input name.<br>

![image](https://github.com/user-attachments/assets/6f97fa81-614a-4b99-aa66-2b1b0873ad13)<br>
![image](https://github.com/user-attachments/assets/8346ffa4-7f67-44a7-9acf-70f884d2fc9d)<br>
![image](https://github.com/user-attachments/assets/baa93415-82ab-4f76-9d83-fafc2543b3ec)<br>
![image](https://github.com/user-attachments/assets/a28610b3-b330-4f73-a3eb-e6d131e8c0d7)<br>







