from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(False, margin=0)

df = pd.read_csv("invoices/10001-2023.1.18.xlsx")