import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# using glob to create list
filepaths = glob.glob("invoices/*.xlsx")

# read the file path
for filepath in filepaths:

    # make pdf
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    # find the file name from the filepath
    filename = Path(filepath).stem
    invoice_nr, Date = filename.split('-')

    # Style the page
    pdf.set_font(family='Times', size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)

    pdf.set_font(family='Times', size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {Date}", ln=1)

    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    # Add header
    columns = df.columns
    columns = [item.replace('-', ' ').title() for item in columns]

    pdf.set_font(family='Times', size=15 , style='B')
    pdf.cell(w=25, h=9, txt=columns[0], border=1)
    pdf.cell(w=60, h=9, txt=columns[1], border=1)
    pdf.cell(w=45, h=9, txt=columns[2], border=1)
    pdf.cell(w=35, h=9, txt=columns[3], border=1)
    pdf.cell(w=30, h=9, txt=columns[4], border=1, ln=1)

    for key, row in df.iterrows():
        # Add Rows of the table
        pdf.set_font(family='Times', size=15)
        pdf.cell(w=25, h=9, txt=str(row['product_id']), border=1)
        pdf.cell(w=60, h=9, txt=str(row['product_name']), border=1)
        pdf.cell(w=45, h=9, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=35, h=9, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=9, txt=str(row['total_price']), border=1, ln=1)

    pdf.output(f"PDF/{filename}.pdf")
