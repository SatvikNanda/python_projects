# Invoice PDF Generator

## Overview:
The Invoice PDF Generator project is a Python application that reads data from Excel files containing invoice details and generates PDF documents for each invoice. The project uses the fpdf library to create and format the PDF files, automating the process of invoice generation. This tool is useful for businesses that need to convert invoice data from Excel sheets into a professional PDF format.

## Features:
Excel to PDF: Convert invoice data from Excel files into structured PDF documents.<br>
Dynamic Invoice and Date Generation: Automatically extract and display the invoice number and date from the file name.<br>
Customizable Table Layout: Generate tables in the PDF with headers and data dynamically populated from the Excel sheet.<br>
Total Price Calculation: Calculate and display the total price of the items in the invoice.<br>
Batch Processing: Process multiple Excel files at once and generate corresponding PDF files.<br>

## Methodology:

Read Excel Files: The program uses glob to find all Excel files in the invoices directory and reads each file using pandas.<br>
Initialize PDF: A new PDF document is created for each invoice using the fpdf library.<br>
Extract Invoice Information: The invoice number and date are extracted from the file name.<br>
Add Header and Footer: Headers and footers are added to the PDF, including the invoice number, date, and total sum.<br>
Generate Table: A table is created in the PDF with data from the Excel file.<br>
Save PDF: The generated PDF is saved in the PDFs directory.<br>

## Excel table layout:
<br>
![image](https://github.com/SatvikNanda/python_projects/assets/93463188/05f0d447-8fe4-4e04-a033-9b6ae4b1f2d7)


## Output:
<br>
![image](https://github.com/SatvikNanda/python_projects/assets/93463188/ec1a935f-3f81-41ec-8071-e902b8577804)
