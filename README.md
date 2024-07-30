# PDF Invoice Generator from Excel Documents

This project is a Python script that generates PDF invoices from Excel files. The script reads data from Excel files located in the `invoices/` directory, processes the data, and generates a PDF invoice for each file. The generated PDFs are saved in the `PDF/` directory.

## Prerequisites

To run this project, you need to have the following Python packages installed:

- pandas
- fpdf
- pathlib

You can install the required packages using pip:

```bash
pip install pandas fpdf pathlib
```

# Project Structure
.
├── invoices/           # Directory containing the Excel invoice files

├── PDF/                # Directory where the generated PDF invoices will be saved

├── pythonhow.png       # Logo image to be included in the PDF

├── generate_pdfs.py    # Python script to generate PDF invoices

└── README.md           # Project readme file


# Script Details

The generate_pdfs.py script performs the following steps for each Excel file:

1.Reads the file paths from the invoices/ directory.

2.Extracts the invoice number and date from the filename.

3.Reads the Excel file into a Pandas DataFrame.

4.Creates a PDF file using the fpdf library.

5.Writes the invoice number, date, and invoice data (including headers) to the PDF.

6.Adds a total price row and additional lines to the PDF.

7.Saves the generated PDF file in the PDF/ directory.

# An example Excel file should have the following structure:

| product_id | product_name | amount_purchased | price_per_unit | total_price |
|------------|--------------|------------------|----------------|-------------|
| 1          | Widget       | 10               | 5.00           | 50.00       |
| 2          | Gadget       | 5                | 15.00          | 75.00       |

The generated PDF will include this data, along with the total price and a logo.

# Contact
If you have any questions or suggestions, feel free to reach out at [supremedocs19@gmail.com].
