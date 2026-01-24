from fpdf import FPDF, XPos
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # print(index)
    # print(row)
    pdf.add_page()
    pdf.set_font('Helvetica', size=24, style='B')
    pdf.cell(w=0, h=12, new_x=XPos.LMARGIN, align="L", text=row["Topic"], )
    pdf.line(10, 21, 200, 21)






pdf.output("output.pdf")