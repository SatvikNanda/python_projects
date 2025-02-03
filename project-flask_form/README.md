# Overview:
This project demonstrates how to:

    Create a web form using Flask and Jinja2 templates (HTML).
    Handle form submissions with Flask routes (GET and POST).
    Save the submitted data in a SQLite database using SQLAlchemy.
    Send automatic email acknowledgments using Flask-Mail.
    Provide immediate feedback to the user via Flask's flash messages.

This can be extended to various use cases such as job applications, contact forms, feedback, or any scenario where you need to collect and store user data and send out email confirmations.

# Features:
1. Form Submission: 
Collects first name, last name, email, available start date, and occupation.

2. Data Persistence:
Utilizes an SQLite database (data.db) to store form entries.

3. Email Notification:
Sends an acknowledgement email to the user upon form submission. The email includes the user’s entered data.

4. Flash Messages:
Displays success messages on the form page once the form is submitted.

5. Bootstrap Styling:
Uses Bootstrap to provide a clean and responsive design for the form.

# Methodology:
1. Flask Setup:

    The application is initialized using Flask.
    The SECRET_KEY is set to handle flash messages securely.

2. Database Configuration:

    A SQLite database URI is configured.
    SQLAlchemy is used for Object Relational Mapping (ORM).

3. Mail Configuration:

    Flask-Mail is set up with Gmail’s SMTP server details.
    Email credentials (username, password) are stored in the Flask app config.

4. Form Handling & Routes:

    The index() function in app.py handles both GET and POST requests.
    For POST requests, the form data is validated, stored in the database, and an email is sent.
    For GET requests, the form is simply rendered (no data submission).

5. Template Rendering:

    index.html is served to the user.
    Bootstrap classes are used for styling.
    Flash messages are displayed to confirm successful submission.

6. Acknowledgment Email:

    Once the user submits the form, Flask-Mail composes an email containing the user’s first name, last name, start date, and occupation.
    The email is sent to the user’s provided address.

# Output:
## Screen Output:
![image](https://github.com/user-attachments/assets/3f9f5e3f-226c-42f5-92b4-17f8d748b4ec)<br>

## Database Output:
![image](https://github.com/user-attachments/assets/2501acd4-cb6e-4445-b26b-3f6977020395)<br>

## Email Output:
![image](https://github.com/user-attachments/assets/0c5cc9da-71a4-4e4c-a392-a485005b3750)


