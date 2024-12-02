# APP NAME
Deliveroo
# GitHub Repository
The source code for this project is available on GitHub: https://github.com/RAYANE8LOUNIS/Deliveroo/tree/main 

## Identification
- **Name:** lounis Rayane
- **P-number:** p448989
- **Course code:** IY499

## Declaration of Own Work
I confirm that this assignment is my own work.
Where I have referred to academic sources, I have provided in-text citations and included the sources in the final reference list.

## Introduction
Deliveroo Order Management System is a Python-based desktop application, I creat and developed this app to make the process of placing, managing, and viewing delivery orders easier. The application is built using a Tkinter library and jnson that makes provision for users to:
_Add customer orders with various delivery options.
_Display the sorted orders by price using bubble sort.
_Securely administer payments with validation for numerous types of payments( credit card , debit card , paypal)
_Allow potential riders to apply to join the delivery service via a rider application form.
This system is perfect for small-scale delivery businesses or an educational project that concentrates on GUI applications and order management.

## Installation
To run the app , ensure you have Python 3.7 or above installed, and then install the required dependencies from the `requirements.txt` file using the following command:
```bash
pip install -r requirements.txt
```
Note: The project currently uses standard Python libraries (tkinter, datetime, json), so no additional dependencies are needed.


## How to run the app 
Run the application by executing the following in your terminal:


python main.py
Features:

Fill in the customer's details: name, address, item, and delivery preference, and click "Add Order" to create a new order.
Confirm the payment for delivery orders through various means, for example, PayPal, Credit/Debit cards.
Click "View Orders" to display all orders sorted by price in descending order.
Click "Apply to be a Rider" to apply to be a delivery rider.


### Running the app
```python
python main.py
```

### Running Unit Tests
```python
python UnitTest.py
```
The project includes a testing module to validate various functionalities. To run unit tests, execute the following:

"python UnitTest.py"  
This command will execute all test cases defined in the UnitTest.py file.

## app Elements
The core elements of my Deliveroo app are:

Customer Order Form:

A form that allows the user to enter customer information: name, address, and preferences for delivery.
The user can select items to deliver.

Order List Viewer:

It lists all the saved orders.
Orders automatically sort in descending order of price using a bubble sort algorithm.
Payment Processing:

Validates the means of payment, including:

Credit/Debit Cards: The card number and date of expiration must be valid.
PayPal: Offers a choice to handle the payment process securely.

Rider Application Form:

A special form for new riders to apply to the delivery service.
Personal information includes name, contact information, and availability.
Error Handling and Validation:

Ensures validation of the user's input in the form fields; for example, no empty fields or incorrect details regarding payments.
Show error messages upon invalid input.

Data Management:

Orders and rider applications will be stored in a JSON file: orders.json.
Persisted data allows the application to reload saved orders when the application is restarted.y 

## Libraries Used
The following libraries are used in this project:

Tkinter: For creating the GUI.
Datetime: To manage timestamps and validate expiration dates for payments.
JSON: For storing and retrieving order data.
OS: For file handling, such as checking and creating orders.json if it doesn't exist.



## Project Structure
- `ErrorHandling/`: Contains classes for handling various errors.
main.py: The main script containing the application logic.
orders.json: A file used to store all customer order data.
ErrorHandling/:  Directory for custom error-handling classes or functions (if applicable).

## Unit Tests (optional)
The project includes xxyy

To run the unit tests, navigate to the project directory and xxyy

This will run all the test cases defined in the `UnitTest.py` file.
