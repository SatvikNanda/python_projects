# Overview:
The Hotel Booking System is a Python-based application that allows users to book hotels by validating their payment information and updating availability. It demonstrates the integration of file-based data storage with a user-friendly interface for managing hotel reservations. The application is suitable for understanding object-oriented programming concepts and data manipulation using pandas.<br>

# Features:
1. Hotel Availability Check: Users can check the availability of a hotel by providing its ID.

2. Hotel Booking: Allows users to book a hotel, marking it as unavailable in the records.

3. Reservation Ticket: Generates a reservation ticket containing the customer's name and hotel details.

4. Payment Validation:<br>
   a. Validates credit card details (number, expiration date, CVV, and holder name).<br>
   b. Authenticates the user with a secure password.


# Methodology:
1. Technologies Used:<br>
  a. Python: Programming language for the application logic.<br>
  b. Pandas: For data manipulation and file handling.

2. Code Structure:<br>
  a. Hotel Class: Manages hotel data, including availability and booking.<br>
  b. ReservationTicket Class: Generates a booking confirmation for the customer.<br>
  c. CreditCard Class: Validates credit card information.<br>
  d. SecureCreditCard Class: Inherits from CreditCard and adds password authentication for enhanced security.

3. Application Workflow:<br>
  a. Users provide the hotel ID to check availability.<br>
  b. If available, the user provides credit card details for validation.<br>
  c. If validation succeeds, the user enters the card password for authentication.<br>
  d. Upon successful authentication, the hotel is marked as booked, and a reservation ticket is generated.


# Output:
The application provides clear and concise outputs for each operation:<br>
![image](https://github.com/user-attachments/assets/e1921a95-805c-40ee-bae2-8e98e81db008)



