from fpdf import FPDF
import pandas as pd
import glob

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)

# pdf = FPDF(orientation="P", unit="mm", format="A4")
# pdf.set_auto_page_break(False, margin=0)
#
# df = pd.read_csv("invoices/10001-2023.1.18.xlsx")