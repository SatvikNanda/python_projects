import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

#running a for loop for the different invoices we have
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    #creating pdf structure/layout
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")

    #generating invoice_no. dynamically
    filename = Path(filepath).stem #stem function extracts the filename from the path of the file
    invoice_no = filename.split("-")[0] #split the name when you find the "-" and take the first element of the list
    pdf.cell(w=50, h=8, txt=f"Invoice No: {invoice_no}", ln=1)

    #generating the date dynamically
    date = filename.split("-")[1] #this time we are getting the second element
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    #adding the header of the table
    header = list(df.columns)
    header = [item.replace("_", " ").title() for item in header]
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=header[0], border=1)
    pdf.cell(w=60, h=8, txt=header[1], border=1)
    pdf.cell(w=40, h=8, txt=header[2], border=1)
    pdf.cell(w=30, h=8, txt=header[3], border=1)
    pdf.cell(w=30, h=8, txt=header[4], border=1, ln=1)

    #Adding the table from excel to pdf
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=60, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    #Adding the total price
    total_sum = df["total_price"].sum()
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=60, h=8, txt="", border=1)
    pdf.cell(w=40, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    #Adding final line
    pdf.set_font(family="Times", size=14, style="B")
    pdf.cell(w=30, h=8, txt=f"The total sum is {total_sum}", ln=1)

    #getting the output
    pdf.output(f"PDFs/{filename}.pdf")
    