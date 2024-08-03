# PDF generator 

## Overview:
The PDF Generator project is a Python application that reads data from a CSV file and generates a PDF document with headers and footers based on the content of the CSV file. The project uses the fpdf library to create and manipulate PDF files. This tool is useful for automating the creation of PDF documents with consistent formatting.

## Features:
CSV to PDF: Convert data from a CSV file into a structured PDF document. <br>
Custom Headers and Footers: Add headers and footers to each page based on the CSV content. <br>
Multi-page PDF: Handle multi-page documents by adding additional pages as specified in the CSV. <br>
Custom Formatting: Set custom fonts, colors, and styles for the PDF content. <br>

## Methodology:
Read CSV File: The program reads data from a CSV file using the pandas library.<br>
Initialize PDF: A new PDF document is created using the fpdf library.<br>
Add Pages: For each row in the CSV, the program adds a new page to the PDF.<br>
Set Header: The header is added at the top of each page with custom font, style, and color.<br>
Set Footer: The footer is added at the bottom of each page with custom font, style, and color.<br>
Save PDF: The final PDF is saved to the specified output file.<br>

## Output: <br>
![image](https://github.com/user-attachments/assets/66a5561a-af22-4f49-b375-d47a7c3ba419) <br>

![image](https://github.com/user-attachments/assets/a8e52505-dd71-45a2-9cae-f4ed4e46a3fc)
